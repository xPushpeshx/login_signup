from django.contrib import messages
from django.shortcuts import render ,HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as authlogin
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm

def login(request):
    if request.method=='POST':
        lfm=AuthenticationForm(request=request,data=request.POST)
        if lfm.is_valid():
            uname=lfm.cleaned_data['username']
            psswd=lfm.cleaned_data['password']
            user=authenticate(username=uname,password=psswd)
            if user is not None:
                authlogin(request,user)
                messages.success(request,"Logged in")
                return HttpResponseRedirect('/profile/')
    else:
        lfm=AuthenticationForm()
    return render(request,'index.html',{'lform':lfm})

def signup(request):
    if request.method=='POST':
        sfm=SignUpForm(request.POST)
        if sfm.is_valid():
            messages.success(request,"Created succesfully")
            sfm.save()
    else:
        sfm=SignUpForm()
    return render(request , 'signup.html',{'sform':sfm})

def profile(request):
    return render(request,'profile.html')
