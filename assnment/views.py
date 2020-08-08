from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
#from .models import information,logoutinfrmation
from django.contrib.auth.models import User
def index(request):
    if not request.user.is_authenticated:
        return render(request,"login/login.html",{"message":None})
    context={
        "user":request.user
            }

    return render(request,"assnment/user.html",context)

def login1(request):
    username=request.POST["username"]
    password=request.POST["password"]
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        #if information.objects.get(userid=User.id):

            #p=information(userid='User.Id',username='User.Username')
            #p.save()
        #else:
         #   q=information(userid='User.Id',username='User.Username')
          #  q.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request,"login/login.html",{"message":"invalid credentials "})

def logout1(request):
    logout(request)
    return render(request,"login/login.html",{"message":"logged out"})

def register(response):
    if response.method=="POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
        return render(response,"assnment/register.html",{"form":form})

# Create your views here.
#def login1(response):
   # return render(response,"assnment/login.html")