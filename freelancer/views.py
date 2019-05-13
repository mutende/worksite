from freelancer.forms import FreelancerChangePasswordForm, FreelancerProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from authentication.decorators import freelancer_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from client.models import Task

# Create your views here.

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