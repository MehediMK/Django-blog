from django.shortcuts import render,get_object_or_404

from .models import allpost
# Create your views here.
def blog(request):
    postdata=allpost.objects.all()
    return render(request,'bloghome.html',{'post':postdata})

def details(request,post_id):
    post_view=get_object_or_404(allpost,pk=post_id)
    return render(request,'details.html',{'post_view':post_view})
