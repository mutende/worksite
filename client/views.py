from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect,get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView
from client.forms import ClientChangePasswordForm, ClientProfileForm, PostTaskForm,CommentForm
from worksiteadmin.models import SkillSet,EducationLevelSet
from freelancer.models import Bid,Completed,FreelancerAccountSummery
from freelancer.forms import CompleteTaskRatingForm
from authentication.decorators import client_required
from authentication.models import User
from client.models import Task,ClientComment
from mpesa.implementation.lipanampesa import lipa_na_mpesa


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
		print(phone_number+'clients phone number')
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
            amount = request.POST['price']
            lipa_na_mpesa(request.user.phone_number,amount)
            task = form.save(commit=False)
            task.client = request.user			
            task.save()
            messages.success(request,('Your task has been posted'))
            return redirect('post_task')
    else:
        form = PostTaskForm(instance= request.user)
    context = {'form': form}

    return render(request, 'client/post_tasks.html', context)

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
			return redirect('client_comment')
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
	bids = Bid.objects.filter(task__client = request.user).filter(task__show=True)
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
	return render(request, 'client/freelancer_profile.html', {'profile':profile})

@login_required
@client_required
def completed_tasks(request):
	completed_tasks = Completed.objects.filter(bid__task__client=request.user).filter(complete = True).filter(rated=False)
	return render(request, 'client/completed_tasks.html',{'completed_tasks':completed_tasks})

@login_required
@client_required
def complete_task_details(request, complete_id, freelancer_id,task_amount):
	form = CompleteTaskRatingForm(request.POST or None)
	detailed = Completed.objects.get(pk=complete_id)
	if request.method == 'POST':		
		if form.is_valid():
			update_rating = Completed.objects.get(pk=complete_id)
			new_rating = request.POST['rating']
			update_rating.rating = new_rating
			update_rating.rated = True		
			update_rating.save()
			#populate the payments table
			payment_status = FreelancerAccountSummery()
			payment_status.amount = task_amount
			payment_status.client= request.user
			#get the freelancer from the table
			freelancer = User.objects.get(pk=freelancer_id)
			payment_status.freelancer = freelancer
			payment_status.save()
			form = CompleteTaskRatingForm()
			return redirect('complete_tasks')

	context = {'detailed':detailed, 'form':form}	
	return render(request, 'client/complete_task_details.html', context)