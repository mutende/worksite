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

    # def __init__(self, *args, **kwargs):
    #     super(ClientSignUpForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['username'].label=''
    #     self.fields['username'].widget.attrs['placeholder'] = 'User Name'
    #     self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].label=''
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Password'
    #     self.fields['password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li></ul>'

    #     self.fields['password2'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].label=''
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
    #     self.fields['password2'].help_text='<span class="form-text text-muted"><span><small>Enter the same password as before, for verification.</small></span>'


    # set user to be client
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
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
    # EducationLevel = forms.ModelMultipleChoiceField(
    #     queryset=EducationLevelSet.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    #     )
    # Skills = forms.ModelMultipleChoiceField(
    #     queryset=SkillSet.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    #     )
    certificate = forms.FileField(required=False)


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name','email','phone_number','address','highest_education_level','best_skill','certificate','password1','password2')


    # set user to freelancer
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_freelancer = True
        if commit:
            user.save()
        return user
