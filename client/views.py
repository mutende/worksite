from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from client.forms import ClientChangePasswordForm, ClientProfileForm, PostTaskForm,CommentForm
from worksiteadmin.models import SkillSet,EducationLevelSet
from client.models import Task,ClientComment
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from authentication.decorators import client_required


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
	#messages.success(request,('You have  been logged out'))
	return redirect('welcome')

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
            task.save()
            messages.success(request,('Your task has been posted'))
            return redirect('post_task')
    else:
        form = PostTaskForm(instance= request.user)
    context = {'form': form}

    return render(request, 'client/post_tasks.html', context)

@method_decorator([login_required, client_required], name='dispatch')
class POST_TASK(CreateView):
	model  =  Task
	form_class = PostTaskForm
	template = 'client/post_tasks.html'
	success_url = 'post_task'

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