from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages

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