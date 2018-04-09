from django.contrib import admin
from .models import Radioitem,City,Country

class RadioitemAdmin(admin.ModelAdmin):
    list_display = 'radio_name','radio_view','radio_likes','created','changed'

class CityAdmin(admin.ModelAdmin):
    list_display = 'name', 'country'

class CountryAdmin(admin.ModelAdmin):
    list_display = 'name',

admin.site.register(City,CityAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(Radioitem,RadioitemAdmin)