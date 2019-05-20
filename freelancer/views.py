from freelancer.forms import FreelancerChangePasswordForm, FreelancerProfileForm,CommentForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from authentication.decorators import freelancer_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView
from django.contrib import messages
from client.models import Task
from django.utils.decorators import method_decorator
from datetime import datetime, date

# Create your views here.
@method_decorator([login_required, freelancer_required], name='dispatch')
class FreelancerHome(TemplateView):
    template_name = 'freelancer/home.html'


def loginFreelancer(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#user object
		user = authenticate(request, username= username, password=password)

		if user is not None:
			login(request, user)
			# messages.success(request,('You have  been logged in successfully'))
			return redirect('freelancer_home')
		else:
			#return some error message
			messages.success(request,('Error loggin in, Username or password invalid please try again ....'))
			return redirect('login_freelancer')
	else:
		return render(request, 'freelancer/login.html')


def logoutFreelancer(request):
	logout(request)
	messages.success(request,('You have  been logged out'))
	return redirect('welcome')

@login_required
@freelancer_required
def freelancer_profile(request):
	if request.method == 'POST':
		form = FreelancerProfileForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request,('You have edited your profile'))
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
	tasks = Task.objects.all()
	context = {'tasks':tasks}
	return render (request, 'freelancer/view_tasks.html',context)

@method_decorator([login_required, freelancer_required], name='dispatch')
class ViewTask(ListView):
	context_object_name = 'tasks'
	template_name='freelancer/view_tasks.html'
	def get_queryset(self):
		today = date.today()
		print('today is on',today)
		return Task.objects.filter(expiry_date__gte=today)

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