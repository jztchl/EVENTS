from django.shortcuts import render
from app.models import *
from django.http import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactmsg(request):
     name = request.GET.get('name')
     mail = request.GET.get('mail')
     subject = request.GET.get('subject')
     msg = request.GET.get('msg')
     a=contactMessage(name=name,email=mail,subject=subject,message=msg)
     a.save()
     return JsonResponse("s")