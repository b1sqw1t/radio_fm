from django.contrib import admin
from .models import Radioitem

class RadioitemAdmin(admin.ModelAdmin):
    list_display = 'radio_name','radio_view','radio_likes','created','changed'
# Register your models here.

admin.site.register(Radioitem,RadioitemAdmin)