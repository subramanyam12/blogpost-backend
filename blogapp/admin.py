from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Blog)
@admin.register(Blog)
class Blogclass(admin.ModelAdmin):
   list_display=['id','title']
