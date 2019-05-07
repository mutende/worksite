from django.contrib import admin
from authentication.models import User
from worksiteadmin.models import EducationLevelSet, SkillSet

# Register your models here.
admin.site.register(User)
# admin.site.register(Client)
# admin.site.register(Freelancer)
admin.site.register(EducationLevelSet)
admin.site.register(SkillSet)

admin.site.site_header= 'Worksite Admin'
