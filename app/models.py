from django.db import models

# Create your models here.
class contactMessage(models.Model):
     name=models.CharField(max_length=100, default='')
     email=models.CharField(max_length=100, default='')
     subject=models.CharField(max_length=500, default='')
     message=models.TextField(max_length=500, default='')
     def __str__(self):
            return f"{self.name}"
     
class event(models.Model):
    name=models.CharField(max_length=100, default='')
    description=models.CharField(max_length=200, default='')
    image=models.ImageField(upload_to='images',default='')
    def __str__(self):
        return f"{self.name}"