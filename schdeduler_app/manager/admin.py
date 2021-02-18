from django.contrib import admin

# Register your models here.
from manager.models import Event, Country

admin.site.register(Event)
admin.site.register(Country)