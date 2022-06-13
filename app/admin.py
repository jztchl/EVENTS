from django.contrib import admin

# Register your models here.
from .models import contactMessage,event
# Register your models here.
admin.site.register(contactMessage)
admin.site.register(event)
