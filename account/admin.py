from django.contrib import admin
from account.models import Profile
from django.conf import settings

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','birthday', 'other_info']

admin.site.register(Profile,ProfileAdmin)

# Register your models here.
