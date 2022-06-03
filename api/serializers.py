import datetime
from django.utils import timezone
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
class docapptserializer(serializers.ModelSerializer):
    appt_date=date_timeserializer()
    
    class Meta:
        model=appointment
        fields=['appt_date','status','patient']
class patapptserializer(serializers.ModelSerializer):
    appt_date=date_timeserializer()
    
    class Meta:
        model=appointment
        fields=['appt_date','status','doctor']
class dochomeapptserializer(serializers.ModelSerializer):
    appt_date=date_timeserializer()
    patient=patientserializer()
    class Meta:
        model=home_appointment
        fields=['appt_date','status','patient']
class pathomeapptserializer(serializers.ModelSerializer):
    appt_date=date_timeserializer()
    doctor=doctorserializer()
    class Meta:
        model=home_appointment
        fields=['appt_date','status','doctor']