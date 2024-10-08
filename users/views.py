from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
# Create your views here.

def profiles(request):
    profiles=Profile.objects.all()
    context={'profiles':profiles}
    return render(request,'users/profiles.html',context=context)

def userProfile(request,pk):
    profile=Profile.objects.get(id=pk)
    topSkills=profile.skill_set.exclude(desc__exact="")
    otherSkills=profile.skill_set.filter(desc="")
    context={'profile':profile,'topSkills':topSkills,'otherSkills':otherSkills}
    return render(request,'users/user-profile.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"Username does not exist")

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,"Username or password is incorrect")

    return render(request,'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request,"Username was successfully logged out ")
    return redirect('login')