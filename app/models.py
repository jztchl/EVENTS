from django.db import models

# Create your models here.
class contactMessage(models.Model):
     name=models.CharField(max_length=100, default='')
     email=models.CharField(max_length=100, default='')
     subject=models.CharField(max_length=500, default='')
     message=models.ImageField(upload_to='images',default='')
    
     
class events(models.Model):
    name=models.CharField(max_length=100, default='')
    description=models.CharField(max_length=500, default='')
    image=models.ImageField(upload_to='images',default='')