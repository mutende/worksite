from django.shortcuts import render

# Create your views here.

def freelancerHome(request):
    return render(request,'freelancer/home.html',{})
