from datetime import date
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.db.models import Avg
from django.shortcuts import render, redirect,get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
from authentication.decorators import client_required
from authentication.models import User
from client.models import Task,ClientComment
from client.forms import ClientChangePasswordForm, ClientProfileForm, PostTaskForm,CommentForm,ReceiveReassignTaskForm
from freelancer.models import Bid,Completed,FreelancerAccountSummery,ReassigendTask,CompletedReassignedTask
from freelancer.forms import CompleteTaskRatingForm,ReassingTaskForm
from mpesa.implementation.lipanampesa import lipa_na_mpesa
from mpesa.models import LNMonline
from worksiteadmin.models import SkillSet,EducationLevelSet


# Create your views here.
@method_decorator([login_required, client_required], name='dispatch')
class ClientHome(TemplateView):
    template_name = 'client/home.html'

@login_required
@client_required
def client_profile(request):
	if request.method == 'POST':
		form = ClientProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You have edited your profile'))
			return redirect('client_home')

	else:
		form = ClientProfileForm(instance=request.user)
		phone_number = request.user.phone_number
	context = {'form': form }
	return render(request, 'client/edit_profile.html', context)

@login_required
@client_required
def clientChangePassword(request):
	if request.method == 'POST':
		form = ClientChangePasswordForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request,('Password changed'))
			return redirect('client_home')
	else:
		form = ClientChangePasswordForm(user=request.user)
	context = {'form': form }
	return render(request, 'client/change_password.html', context)

@login_required
@client_required
def post_task_view(request):
    if request.method == 'POST':
        form = PostTaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.client = request.user
            deduct = (25/100)
            price = request.POST.get('price')
            pay = float(price)*float(deduct)
            task.pay = float(price) - float(pay)			
            task.save()
            # messages.success(request,('Your task has been posted, go to your task history and proceed on paying so that your task will be available for bidding'))
            return redirect('client_task_history')
    else:
        form = PostTaskForm(instance= request.user)
    context = {'form': form}

    return render(request, 'client/post_tasks.html', context)

@login_required
@client_required
def pay_for_task(request, task_id):
	task = Task.objects.get(pk=task_id)
	amount=task.price
	phone= request.user.phone_number	
	if request.method == 'POST':
		confirm = request.POST.get("confirm")
		pay= False
		if confirm == "yes":
			pay=True
		else:
			pay = False
		if pay==True:
			lipa_na_mpesa(phone,amount)
			return redirect('confirm_payment', pk=task.id)
		else:
			messages.success(request,'If there was an error with information provided during payment for a task, write  comment with the specific details you want to be updated')
			return redirect('client_comment')
	
	context = {'amount': amount, 'phone': phone, 'task': task}
	return render(request, 'client/pay_for_task.html',context)
	
@login_required
@client_required
def confirm_payment(request,pk):
	if request.method == 'POST':
		transaction_id = request.POST.get('transaction_id')	
		count = LNMonline.objects.values_list('Result_Code').filter(Phone_Number=request.user.phone_number).filter(Mpesa_Receipt_Number=transaction_id).count()
		if count > 1:
			#retun error in inputting id more than 1 id found
			messages.success(request, 'Enter the correct trsanction ID')
			return redirect('confirm_payment', pk=pk)
		elif count == 1:
			#validate and activate task to be viewed by freelancers
			task = Task.objects.get(pk=pk)
			transaction = LNMonline.objects.get(Result_Code=0,Phone_Number=request.user.phone_number,Mpesa_Receipt_Number=transaction_id)
			required_code = 0
			if str(transaction) == str(required_code):
				task.paid = True
				task.save()
				return redirect('client_task_history')
			else:
				messages.success(request, 'Incorrect Transaction Code, or The transaction was not Successful')
				return redirect('confirm_payment', pk=pk)
		else:
			#no id matching
			messages.success(request, 'Transaction ID do not match with any')
			return redirect('confirm_payment', pk=pk)
	return render(request,'client/confirm_payment.html',{})


@login_required
@client_required
def make_a_comment(request):
	form = CommentForm( request.POST or None)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit=False)
			comment.user = request.user
			comment.save()
			messages.success(request,('comment submitted'))
			return redirect('client_home')
		else:
			form = CommentForm()
	context = {'form': form}

	return render(request, 'client/comment.html', context)

@login_required
@client_required
def get_my_tasks(request):
	tasks = Task.objects.filter(client = request.user)
	return render(request,'client/my_tasks.html', {'tasks':tasks})

@login_required
@client_required
def task_bids(request):
	today = date.today()
	bids = Bid.objects.filter(task__client = request.user).filter(task__show=True).filter(task__expiry_date__gt=today)
	return render(request, 'client/view_bids.html', {'bids':bids})

@login_required
@client_required
def assign_task(request, bid_id, task_id):
	bid = Bid.objects.get(pk=bid_id)
	bid.assign = True
	bid.save()
	task = Task.objects.get(pk=task_id)
	task.is_taken=True
	task.show = False
	task.save()
	return redirect('view_bids')

@login_required
@client_required
def freelancer_profile(request, profile_id):	
	profile = User.objects.get(pk=profile_id)
	count = Completed.objects.filter(freelancer = profile).count
	rating =Completed.objects.filter(freelancer=profile).aggregate(rating=Avg('rating'))
	context = {'count':count,'rating':rating,'profile':profile}
	return render(request, 'client/freelancer_profile.html', context)

@login_required
@client_required
def completed_tasks(request):
	completed_tasks = Completed.objects.filter(bid__task__client=request.user).filter(complete = True).filter(re_assigned=False)
	return render(request, 'client/completed_tasks.html',{'completed_tasks':completed_tasks})

@login_required
@client_required
def complete_task_details(request, bid_id, complete_id,freelancer_id,task_amount):
	form = CompleteTaskRatingForm(request.POST or None)
	detailed = Completed.objects.get(pk=complete_id)
	if request.method == 'POST':		
		if form.is_valid():
			update_rating = Completed.objects.get(pk=complete_id)
			new_rating = request.POST['rating']
			update_rating.rating = new_rating
			update_rating.rated = True		
			update_rating.save()			

			#make complete on the bid task to true and check if its late submission
			bid = Bid.objects.get(pk=bid_id)
			today = date.today()
			if bid.task.expiry_date <= today:
				print('Due date = '+str(bid.task.expiry_date))
				print('Today date = '+str(today))
				bid.late_submission = True
				after_fine = float(((0.7)*float(task_amount)))
				fine = float(((0.3)*float(task_amount)))

				#update payment stuffs
				payment_status = FreelancerAccountSummery()
				payment_status.client= request.user
				freelancer = User.objects.get(pk=freelancer_id)
				payment_status.freelancer = freelancer								
				payment_status.amount=after_fine
				payment_status.fines = fine
				print('Differnce in days'+str(today- bid.task.expiry_date))
				print('Pay '+ str(freelancer)+' this amount '+str(after_fine)+' instead of '+str(task_amount)+' after deducting '+str(fine))
				bid.save()
				payment_status.save()
				form = CompleteTaskRatingForm()
				return redirect('complete_tasks')
			if bid.task.expiry_date >= today:
				payment_status = FreelancerAccountSummery()
				payment_status.client= request.user
				freelancer = User.objects.get(pk=freelancer_id)
				payment_status.freelancer = freelancer								
				payment_status.amount=task_amount
				fine = 0.00
				payment_status.fine = float(fine)
				print('Differnce in days '+str(today- bid.task.expiry_date))
				print((today- bid.task.expiry_date))
				print('Pay '+ str(freelancer)+' this amount '+str(task_amount)+' after deducting '+str(fine))
				bid.save()
				payment_status.save()
				form = CompleteTaskRatingForm()
				return redirect('complete_tasks')	
	context = {'detailed':detailed, 'form':form}	
	return render(request, 'client/complete_task_details.html', context)


@login_required
@client_required
def reassign_task(request, bid_id, freelancer_id):
	if request.method == 'POST':
		form = ReassingTaskForm(request.POST, request.FILES)
		if form.is_valid():
			reasssigned  =  form.save(commit=False)
			freelancer= User.objects.get(pk=freelancer_id)	
			client = request.user
			bid = Bid.objects.get(pk=bid_id)
			reasssigned.client = client
			reasssigned.freelancer= freelancer
			reasssigned.bid = bid
			complete = Completed.objects.get(bid = bid_id)
			complete.re_assigned = True
			new_rating = 1.0
			complete.rating = float(new_rating)
			complete.save()
			reasssigned.save()
			return redirect('reassigned_tasks_client')
	form = ReassingTaskForm()
	return render(request, 'client/reassign_task.html', {'form':form})

@login_required
@client_required
def reassigned_task(request):
	tasks = ReassigendTask.objects.filter(client=request.user)
	return render (request,'client/reassigned_tasks.html', {'tasks':tasks})


@login_required
@client_required
def review_reassigned_task(request, bid_id, the_id):
	form = ReceiveReassignTaskForm()
	detailed = CompletedReassignedTask.objects.get(reassigned_task=the_id)
	if request.method == 'POST':
		form = ReceiveReassignTaskForm(request.POST)
		if form.is_valid():
			the_rating = request.POST['rating']
			detailed.rating = the_rating
			detailed.save()

			#make complete in bid to true
			bid = Bid.objects.get(pk=bid_id)
			bid.complete = True
			reassigned_freelancer = bid.freelancer
			payments_for_task = bid.task.pay
			pay_reassigned = float(((0.8) * float(payments_for_task)))
			payments_fines = float(((0.2) * float(payments_for_task)))
			bid.save()

			#populate the payments table and check if there are fines for this individual
			# print('Reassigned freelancer '+str(reassigned_freelancer))
			# print('The real amount '+str(payments_for_task))
			# print('The deducted  amount '+str(pay_reassigned))
			
			payment_status = FreelancerAccountSummery()	
			payment_status.amount = pay_reassigned
			payment_status.client= request.user
			payment_status.freelancer = reassigned_freelancer
			payment_status.fines = payments_fines
			payment_status.save()
			
	context = {'form':form, 'detailed':detailed}
	return render(request, 'client/completed_reassigned_task.html', context)

@login_required
@client_required
def help(request):
	return render(request, 'client/help.html',{})