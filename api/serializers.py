from .models import *
from rest_framework import serializers
class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields='__all__'
class date_timeserializer(serializers.ModelSerializer):
    class Meta:
        model=date_time
        fields='__all__'

class doctorserializer(serializers.ModelSerializer):
   # availablity=dateserializer()
    class Meta:
        model=doctor
        fields=['id','long','lat']
class doctoravaserializer(serializers.ModelSerializer):
    date_time=date_timeserializer()
    class Meta:
        model=doctor_ava
        fields=['date_time']
class apptserializer(serializers.ModelSerializer):
    class Meta:
        model=appointment
        fields=['appt_date','status']
class homeapptserializer(serializers.ModelSerializer):
    class Meta:
        model=home_appointment
        fields=['appt_date','status']
