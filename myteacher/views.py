from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
#@login_required



def home(request):
    user=request.user
    dict={"users":"username","id":"identifier"}
    #passw=request.passw
    if(user=="abc"):
        return render(request,"login.html",{})
    else:
        return render(request,"home.html",dict)

def profile(request):
    return render(request,"profile.html",{'username':request.user.username})


def login(request):
    return render(request,'registration/login.html')