from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from authentication.forms import ClientSignUpForm,FreelancertSignUpForm
from authentication.models import User
from django.urls import reverse_lazy

def signupview(request):
    return render(request, 'directsignup.html')

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
