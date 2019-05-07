from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from worksiteadmin.forms import SkillSet

class WorksiteAdminHome(TemplateView):
    template_name= 'worksiteadmin/landingpage.html'

# def addSkills(request):
#     form = SkillSetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = SkillSetForm()
#     context = {'form':form}
#     return render(request, 'worksiteadmin/addskills.html', context)
# def addEducationLevel(request):
#     form = EducationLevelSetForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = EducationLevelSetForm()
#     context = {'form':form}
#     return render(request, 'worksiteadmin/addEducationLevel.html', context)
