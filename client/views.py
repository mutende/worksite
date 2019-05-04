from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages


# Create your views here.

class ClientHome(TemplateView):
    template_name = 'client/home.html'

#login function
def loginClient(request):
    #if post method is requested from template
	if request.method == 'POST':
        #get credantials 
		username = request.POST['username']
		password = request.POST['password']

		#user object assigned to a function that authenticates
		user = authenticate(request, username= username, password=password)

        #user available in database
		if user is not None:
            #proceed with login
			login(request, user)
			# messages.success(request,('You have  been logged in successfully'))
			return redirect('client_home')
		else:
			#return some error message
			messages.success(request,('Error loggin in, Username or password invalid please try again ....'))
			return redirect('login_client')
	else:
		return render(request, 'client/login.html')

#logout function
def logoutClient(request):
	logout(request)
	messages.success(request,('You have  been logged out'))
	return redirect('welcome')
