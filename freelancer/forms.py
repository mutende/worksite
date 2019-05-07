from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from worksiteadmin.models import SkillSet,EducationLevelSet


class FreelancerChangePasswordForm(PasswordChangeForm):
	class Meta:
		fields = ('old_password','newpassword1','newpassword2')
	def __init__(self, *args, **kwargs):
		super(FreelancerChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].label=''
		self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].label=''
		self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
		self.fields['new_password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].label=''
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].help_text='<span class="form-text text-muted"><span><small>Enter the same password as before, for verification.</small></span>'

class FreelancerProfileForm(UserChangeForm):
	password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
	phoneNumber = forms.CharField(widget=forms.TextInput())
	Address = forms.CharField(widget=forms.TextInput())
	EducationLevel = forms.ModelMultipleChoiceField(
		queryset=EducationLevelSet.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
	)
	Skills = forms.ModelMultipleChoiceField(
		queryset=SkillSet.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
	)
	Certificate = forms.FileField()
	class Meta:
		model = User
		fields = ('email','phoneNumber','Address','EducationLevel','Skills','Certificate','password',)
	def __init__(self, *args, **kwargs):
		super(FreelancerProfileForm, self).__init__(*args, **kwargs)
		self.fields['phoneNumber'].widget.attrs['class'] = 'form-control'
		# self.fields['username'].label='User Name'
		self.fields['phoneNumber'].widget.attrs['placeholder'] = 'Phone Number'
		self.fields['phoneNumber'].help_text='in format of +2547... start with country code'
		

		# self.fields['first_name'].widget.attrs['class'] = 'form-control'
		# # self.fields['first_name'].label=''
		# self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

		# self.fields['last_name'].widget.attrs['class'] = 'form-control'
		# # self.fields['first_name'].label=''
		# self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

		self.fields['Address'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		# self.fields['Address'].widget.attrs['placeholder'] = 'Email'

		# self.fields['Skills'].widget.attrs['class'] = 'form-control'
		# # self.fields['first_name'].label=''
		# self.fields['Skills'].widget.attrs['placeholder'] = 'Email'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		# self.fields['email'].widget.attrs['placeholder'] = 'Email'