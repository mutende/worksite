from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class WorksiteAdminHome(TemplateView):
    template_name= 'worksiteadmin/landingpage.html'
