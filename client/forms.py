from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea
from client.models import Task,ClientComment
from worksiteadmin.models import EducationLevelSet,SkillSet


class ClientChangePasswordForm(PasswordChangeForm):
	class Meta:
		fields = ('old_password','newpassword1','newpassword2')
	def __init__(self, *args, **kwargs):
		super(ClientChangePasswordForm, self).__init__(*args, **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].label=''
		self.fields['old_password'].widget.attrs['placeholder'] = 'Old Password'

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].label=''
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].help_text='<ul class="form-text text-muted small"><li> Your password can\'t be too similar to your other personal information.</li> <li>Your password must contain at least 8 characters.</li> <li>Your password can\'t be a commonly used password.</li> <li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].label=''
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].help_text='<span class="form-text text-muted"><span><small>Enter the same password as before, for verification.</small></span>'

class ClientProfileForm(UserChangeForm):
	password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name','email','password')
	def __init__(self, *args, **kwargs):
		super(ClientProfileForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		# self.fields['first_name'].label=''
		self.fields['email'].widget.attrs['placeholder'] = 'Email'



class PostTaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('title','description','best_skill','highest_education_level','expiry_date','documet_format','task_file','price')
		widgets = {
            'description': Textarea(attrs={'class':'form-control','cols':4, 'rows':5}),
        }
	def __init__(self,*args,**kwargs):
		super(PostTaskForm, self).__init__(*args,**kwargs)
		self.fields['expiry_date'].widget.attrs['readonly'] = True

class CommentForm(forms.ModelForm):
	class Meta:
		model = ClientComment
		fields =('comment',)
		widgets = {
            'comment': Textarea(attrs={'class':'form-control','cols':4, 'rows':5}),
        }
