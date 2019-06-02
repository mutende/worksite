from django.contrib import admin
from authentication.models import User
from worksiteadmin.models import EducationLevelSet, SkillSet
from django.contrib.auth.models import Group
from client.models import Task,ClientComment
from freelancer.models import Comment, Bid,Completed,FreelancerAccountSummery
from mpesa.models import LNMonline


#classes that help display and filter data in the admin panel
class UserAdmin(admin.ModelAdmin):
    fields = ('username','first_name','last_name','email','phone_number','date_joined','address','highest_education_level','best_skill','certificate','is_account_active','is_freelancer','is_client')
    list_display = ('username','is_freelancer','is_client','is_superuser','is_account_active',)
    list_filter =('date_joined','is_account_active','is_client','is_freelancer',)


class TaskAdmin(admin.ModelAdmin):
    list_filter =('date_posted','expiry_date','is_taken','price',)
    list_display =('title','client','date_posted','expiry_date','is_taken','price',)


class CommentAdmin(admin.ModelAdmin):
    list_filter=('comment_date',)
    list_display=('user','comment_date',)
class BidAdmin(admin.ModelAdmin):
    list_display = ('freelancer','task','date','assign',)
    list_filter = ('assign',)
class CompletedAdmin(admin.ModelAdmin):
    list_display = ('freelancer','date','rating','re_assigned','complete',)
    list_filter = ('complete','re_assigned','date',)

class FreelancerAccountSummeryAdmin(admin.ModelAdmin):
    list_display=('freelancer','client','amount','date','paid',)
    list_filter=('paid',)

class LNMonlineAdmin(admin.ModelAdmin):
    list_display=('Transaction_Date','Amount','Mpesa_Receipt_Number','Phone_Number',)
    list_filter=('Transaction_Date',)    


# registered models.
admin.site.register(User,UserAdmin)
admin.site.register(EducationLevelSet)
admin.site.register(SkillSet)
admin.site.unregister(Group)
admin.site.register(Task,TaskAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ClientComment,CommentAdmin)
admin.site.register(Bid,BidAdmin)
admin.site.register(Completed,CompletedAdmin)
admin.site.register(FreelancerAccountSummery,FreelancerAccountSummeryAdmin)
admin.site.register(LNMonline,LNMonlineAdmin)

admin.site.site_header= 'Worksite Admin'
