from django.shortcuts import render

# Create your views here.
def clientHome(request):
    return render(request,'client/home.html',{})
