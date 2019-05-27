from freelancer.forms import FreelancerChangePasswordForm, FreelancerProfileForm,CommentForm,CompleteTaskForm
from django.contrib.auth.decorators import login_required
from authentication.decorators import freelancer_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib import messages
from client.models import Task
from freelancer.models import Bid,Completed
from django.utils.decorators import method_decorator
from datetime import datetime, date
from itertools import chain
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@method_decorator([login_required, freelancer_required], name='dispatch')
class FreelancerHome(TemplateView):
    template_name = 'freelancer/home.html'

@login_required
@freelancer_required
def freelancer_profile(request):
	if request.method == 'POST':
		form = FreelancerProfileForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			# messages.success(request,('You have edited your profile'))
			return redirect('freelancer_home')

	else:
		form = FreelancerProfileForm(instance=request.user)
	context = {'form': form }
	return render(request, 'freelancer/edit_profile.html', context)

@login_required
@freelancer_required
def freelancerChangePassword(request):
	if request.method == 'POST':
		form = FreelancerChangePasswordForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request,('Password changed'))
			return redirect('freelancer_home')
	else:
		form = FreelancerChangePasswordForm(user=request.user)
	context = {'form': form }
	return render(request, 'freelancer/change_password.html', context)

@login_required
@freelancer_required
def view_tasks(request):
	today = date.today()
	tasks = Task.objects.filter(expiry_date__gte=today)
	context = {'tasks':tasks}
	return render (request, 'freelancer/view_tasks.html',context)

@method_decorator([login_required, freelancer_required], name='dispatch')
class ViewTask(ListView):
	context_object_name = 'tasks'
	template_name='freelancer/view_tasks.html'

	# def get_context_data(self, **kwargs):
	# 	context = super(ViewTask, self).get_context_data(**kwargs)
	# 	tasks = Task.objects.filter(freelancer = user)
	# 	# all_bids = Bid.objects.all()
	# 	# tasks = chain(
	# 	# 	all_bids,
	# 	# 	all_tasks,
	# 	# )

	# 	context.update({
    #         'bids': tasks,
	# 		# 'bidded_tasks':task.		
    #         # 'more_context': Model.objects.all(),
    #     })
	# 	return context

	def get_queryset(self):
		today = date.today()
		# all_tasks = Task.objects.filter(expiry_date__gte=today)
		# all_bids = Bid.objects.all()

		# tasks = chain(
		# 	all_bids,
		# 	all_tasks,
		# )
		return Task.objects.filter(expiry_date__gte=today).filter(is_taken=False)


@method_decorator([login_required, freelancer_required], name='dispatch')
class TaskDetails(DetailView):
	model = Task
	template_name='freelancer/task_details.html'

@login_required
@freelancer_required
def make_a_comment(request):
	form = CommentForm( request.POST or None)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid:
			comment = form.save(commit=False)
			comment.user = request.user
			comment.save()
			messages.success(request,('comment submitted'))
			return redirect('freelancer_comment')
		else:
			form = CommentForm()
	context = {'form': form}

	return render(request, 'freelancer/comment.html', context)

@login_required
@freelancer_required
def make_a_bid(request, task_id):
	new_task = get_object_or_404(Task, pk=task_id)
	new_freelancer = request.user
	bid = Bid()
	bid.task = new_task
	bid.freelancer= new_freelancer
	bid.save()
	return redirect('view_tasks')

@login_required
@freelancer_required
def get_assigned_tasks(request):
	my_tasks = Bid.objects.filter(freelancer = request.user).filter(assign = True)
	return render(request, 'freelancer/my_tasks.html', {'my_tasks':my_tasks})

@login_required
@freelancer_required
def submit_a_task(request, bid_id):
	if request.method == 'POST':
		form = CompleteTaskForm(request.POST, request.FILES)
		if form.is_valid:
			complete = form.save(commit=False)
			complete.bid = Bid.objects.get(pk=bid_id)
			complete.complete = True
			complete.freelancer = request.user
			complete.save()
			# alter data on bids table
			alter_bid = Bid.objects.get(pk=bid_id)
			alter_bid.show = False
			alter_bid.save()
			return redirect('assigned')
	else:
		form = CompleteTaskForm()

	context = {'form': form}
	return render(request, 'freelancer/submit_task.html', context)
	
		
