from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from worksiteadmin.models import SkillSet,EducationLevelSet
from django.forms import Textarea
from freelancer.models import Comment,Completed,CompletedReassignedTask,ReassigendTask


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
		self.fields['new_password1'].help_text=''

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].label=''
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].help_text=''

class FreelancerProfileForm(UserChangeForm):
	email = forms.CharField(widget=forms.TextInput(),required=True)
	password = forms.CharField(widget=forms.TextInput(attrs={'type':'hidden'}))
	phone_number = forms.CharField(widget=forms.TextInput())
	address = forms.CharField(widget=forms.TextInput())
	highest_education_level = forms.CharField(widget=forms.TextInput(), required=False)
	# highest_education_level = forms.ModelChoiceField(
	# 		queryset=EducationLevelSet.objects.all(),
    #     # widget=forms.CheckboxSelectMultiple,
    #     required=False
	# )
	best_skill=forms.CharField(widget=forms.TextInput(), required=False)
	# best_skill = forms.ModelChoiceField(
	# 	queryset=SkillSet.objects.all(),
    #     # widget=forms.CheckboxSelectMultiple,
    #     required=False
	# )
	certificate = forms.FileField(required=False)
	class Meta:
		model = User
		fields = ('email','phone_number','address','certificate','password',)
	def __init__(self, *args, **kwargs):
		super(FreelancerProfileForm, self).__init__(*args, **kwargs)
		if kwargs.get('instance'):
			#get initial selected value
			initial = kwargs.setdefault('initial',{})
			#list of primary key of selected data
			if kwargs['instance'].highest_education_level:
				initial['highest_education_level'] = kwargs['instance'].highest_education_level
			else:
				initial['highest_education_level']=None
			#get initial selected value
			initial = kwargs.setdefault('initial',{})
			#list of primary key of selected data
			if kwargs['instance'].best_skill:
				initial['best_skill'] = kwargs['instance'].best_skill
			else:
				initial['best_skill']=None
		forms.ModelForm.__init__(self,*args, **kwargs)
		self.fields['phone_number'].help_text='in format of 2547... start with country code without the plus'
		self.fields['highest_education_level'].widget.attrs['readonly'] = True
		self.fields['best_skill'].widget.attrs['readonly'] = True
		self.fields['best_skill'].help_text='you cannot edit your level of education immediately, just upload your  new certificate and the admin will update skills and education level'

		# self.fields['address'].widget.attrs['class'] = 'form-control'
		# self.fields['email'].widget.attrs['class'] = 'form-control'

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields =('comment',)
		widgets = {
            'comment': Textarea(attrs={'class':'form-control','cols':4, 'rows':5}),
        }
class CompleteTaskForm(forms.ModelForm):
	class Meta:
		model = Completed
		fields = ('file','description',)

class CompleteTaskRatingForm(forms.ModelForm):
	class Meta:
		model = Completed
		fields =('rating',)
class ReassingTaskForm(forms.ModelForm):
	class Meta:
		model = ReassigendTask
		fields = ('reasons','file',)
		widgets = {
            'reasons': Textarea(attrs={'class':'form-control','cols':4, 'rows':5}),
        }
class SubmitReassignedTaskForm(forms.ModelForm):
	class Meta:
		model = CompletedReassignedTask
		fields = ('revised_file',)
	def __init__(self, *args, **kwargs):
		super(SubmitReassignedTaskForm, self).__init__(*args, **kwargs)
		forms.ModelForm.__init__(self,*args, **kwargs)
		self.fields['revised_file'].widget.attrs['required'] = True