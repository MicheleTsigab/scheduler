import datetime
from django.utils import timezone
from .models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
class patientserializer(GeoFeatureModelSerializer):
    class Meta:
        model=patient
        fields=['id','location']
        geo_field = 'location'
class date_timeserializer(serializers.ModelSerializer):
    class Meta:
        model=date_time
        fields='__all__'

class doctorserializer(GeoFeatureModelSerializer):
   # availablity=dateserializer()
    class Meta:
        model=doctor
        fields=['id','location']
        geo_field = 'location'
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