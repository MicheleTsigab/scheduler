from django.contrib import admin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.
#admin.site.register(patient)
#admin.site.register(doctor)
admin.site.register(date_time)
admin.site.register(appointment)
admin.site.register(home_appointment)
admin.site.register(doctor_ava)
@admin.register(doctor)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('id', 'location')