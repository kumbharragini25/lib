from django.contrib import admin
from homepage.models import myhome
from django.conf import settings
class homeadmin(admin.ModelAdmin):
    list_display=('title','image')
admin.site.register(myhome,homeadmin)    
# Register your models here.
