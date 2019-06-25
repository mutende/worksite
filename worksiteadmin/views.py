from datetime import datetime, date
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from worksiteadmin.utils import render_to_pdf
from authentication.models import User
from freelancer.models import Bid

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
@permission_required('admin.can_add_log_entry')
def report_home(request):
    return render(request, 'admin/report_home.html',{})

@permission_required('admin.can_add_log_entry')
def admin_help(request):
    return render(request, 'admin/help.html',{})

@permission_required('admin.can_add_log_entry')
def generate_freelancers_pdf(request):
    to_day = date.today()
    freelacers = User.objects.filter(is_freelancer=True)
    data = {
            'to_day': to_day,
            'freelacers':freelacers,
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
    pdf = render_to_pdf('pdfs/freelancers.html', data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "freelancers.pdf"
        content = "inline; filename='%s'" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
    return HttpResponse(pdf, content_type='application/pdf')


@permission_required('admin.can_add_log_entry')
def freelancers_report(request):
    today = date.today()
    freelancers = User.objects.filter(is_freelancer=True)
    return render(request, 'admin/freelancers_report.html', {'freelancers':freelancers, 'today':today})
