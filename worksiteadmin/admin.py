from django.contrib import admin
from authentication.models import User
from worksiteadmin.models import EducationLevelSet, SkillSet
from django.contrib.auth.models import Group
from client.models import Task



class UserAdmin(admin.ModelAdmin):
    fields = ('username','first_name','last_name','email','phone_number','date_joined','address','highest_education_level','best_skill','certificate','is_account_active','is_freelancer','is_client')
    list_display = ('username','is_freelancer','is_client','is_account_active',)
    list_filter =('date_joined','is_account_active','is_client','is_freelancer',)


class TaskAdmin(admin.ModelAdmin):
    list_filter =('date_posted','expiry_date','is_taken')
    list_display =('title','date_posted','expiry_date','is_taken',)

# Register your models here.
admin.site.register(User,UserAdmin)
admin.site.register(EducationLevelSet)
admin.site.register(SkillSet)
admin.site.unregister(Group)
admin.site.register(Task)

admin.site.site_header= 'Worksite Admin'
