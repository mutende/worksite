from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from authentication.models import User
from worksiteadmin.models import SkillSet,EducationLevelSet

#client form
class ClientSignUpForm(UserCreationForm):
    phone_number = forms.CharField(max_length=13,widget=forms.TextInput())
    address = forms.CharField(required=False, max_length=100, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    first_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput())
    last_name = forms.CharField( max_length=100, required=True, widget=forms.TextInput())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','email','phone_number','address','password1','password2')

    def __init__(self, *args, **kwargs):
        super(ClientSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''

    # set user to be client and make account actve
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.is_account_active = True
        if commit:
            user.save()
        return user

#freelancer form
class FreelancertSignUpForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput())
    address = forms.CharField(max_length=13,required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    first_name = forms.CharField(max_length=100,required=True, widget=forms.TextInput())
    last_name = forms.CharField( max_length=100, required=True, widget=forms.TextInput())
    certificate = forms.FileField(required=False)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','email','phone_number','address','highest_education_level','best_skill','certificate','password1','password2')
    
    def __init__(self, *args, **kwargs):
        super(FreelancertSignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text=''
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''

    # set user to freelancer
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_freelancer = True
        if commit:
            user.save()
        return user
