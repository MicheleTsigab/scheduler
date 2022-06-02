from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(patient)
admin.site.register(doctor)
admin.site.register(date_time)
admin.site.register(appointment)
admin.site.register(home_appointment)
admin.site.register(doctor_ava)