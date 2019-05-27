from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from authentication.forms import ClientSignUpForm,FreelancertSignUpForm
from authentication.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib import messages

class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'client_signup.html'
    # success_url = reverse_lazy('login_client')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('client_home')

class FreelancerSignUpView(CreateView):
    model = User
    form_class = FreelancertSignUpForm
    # success_url = reverse_lazy('login_freelancer')
    template_name = 'freelancer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'freelancer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('freelancer_home')

#login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_client:
                login(request,user)
                return redirect('client_home')
            elif user.is_freelancer:
                login(request, user)
                return redirect('freelancer_home')
            else:
                login(request,user)
                return redirect('admin:index')
        else:
            messages.success(request,('Error loggin in, Username or password invalid please try again ....'))
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout_user(request):
	logout(request)
	return redirect('welcome')
