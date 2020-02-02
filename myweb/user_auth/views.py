from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib import messages

from .form import RegisterationFrom,EditInfoForm
# Create your views here.

def ulogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully login')
            return redirect('home')
        else:
            messages.success(request,'Please Try again')
            return redirect('login')
    else:
        return render(request,'login.html')
def ulogout(request):
    logout(request)
    messages.success(request,'Successfully Logout')
    return redirect('login')

def usrr_regi(request):
    if request.method == 'POST':
        form = RegisterationFrom(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(request,username=username,password=password)
            login(request, user)
            messages.success(request,'Account created')
            return redirect('home')
    else:
        form= RegisterationFrom()
        contex={
        'form':form
        }
        return render(request,'signup.html',contex)


def editinfo(request):
    if request.method=='POST':
        form = EditInfoForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Information update')
            return redirect('home')
    else:
        form = EditInfoForm(instance=request.user)
        return render(request,'editinfo.html',{'form':form})

def profile(request):
    return render(request,'profile.html')