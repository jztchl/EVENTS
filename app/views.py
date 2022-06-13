from django.shortcuts import render
from app.models import *
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
     if request.method=='POST':
         mail = request.POST['mail']
         name = request.POST['name']
         subject = request.POST['subject']
         msg = request.POST['message']
         a=contactMessage(name=name,email=mail,subject=subject,message=msg)
         a.save()
         return HttpResponseRedirect('/contact')
     else:
         return render(request, 'contact.html')

def blog(request):
    ss = event.objects.all()
    return render(request, 'blog.html',{"eve": ss})

def aboutus(request):
    return render(request, 'aboutus.html')


   