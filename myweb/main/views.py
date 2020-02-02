from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import services

# Create your views here.
def home(request):
    myserv = services.objects.all()
    return render(request,'home.html',{'myserv':myserv})
#@login_required
def contact(request):
    return render(request, 'contact.html')
