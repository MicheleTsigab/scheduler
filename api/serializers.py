from unittest.util import _MAX_LENGTH
from rest_framework import status
from calendar import day_abbr
import datetime
from gc import get_objects
from xmlrpc.client import ResponseError
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields=['id']
        #geo_field = 'location'
class date_timeserializer(serializers.ModelSerializer):
    class Meta:
        model=date_time
        #fields='__all__'
        fields=['date','start_time','end_time']
class doctorserializer(GeoFeatureModelSerializer):
   # availablity=dateserializer()
    class Meta:
        model=doctor
        fields=['id','location','is_home_doctor']
        geo_field = 'location'
class doctoravaserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    #date_time=date_timeserializer()
    class Meta:
        model=doctor_ava
        #fields=['id','doctor','date_time']
        fields='__all__'
    # def create(self, validated_data):
    #     doctor_data=validated_data.get('doctor')
    #     date_time_data = validated_data.pop('date_time')
    #     a = get_object_or_404(doctor, pk=doctor_data.id)
    #     da=date_time.objects.create(**date_time_data)
    #     doctor_availablity= doctor_ava.objects.create(doctor=a, date_time=da)
    #     return doctor_availablity

class apptserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    appt_date=date_timeserializer()
    #temp=serializers.
    class Meta:
        model=appointment
        fields=['id','doctor','appt_date','temp']
        
    def create(self, validated_data):
        doctor_data=validated_data.get('doctor')
        date_time_data = validated_data.pop('appt_date')
        patient_data=validated_data.get('temp')
        status_data=validated_data.get('status')
        pat,sd= patient.objects.get_or_create(id=patient_data)
        doc = get_object_or_404(doctor, pk=doctor_data.id)
        da,created=date_time.objects.get_or_create(**date_time_data)
        
        #print(da)
        available=doctor_ava.objects.filter(days=(da.date.weekday()+1),start_time__lte=da.start_time,end_time__gte=da.end_time)
        if available:
            print("hello")
            #da.save()
        else:
            raise serializers.ValidationError({"detail":"No available working hour"})    
        if appointment.objects.filter(doctor=doc,appt_date=da):
            res=serializers.ValidationError({"detail":"The Date " +str(da.date)+" "+str(da.start_time)+" to "+str(da.end_time) +" is already booked, Try other appointment dates"})
            res.status_code=status.HTTP_409_CONFLICT
            raise res 
        
        else:
            appt= appointment.objects.create(doctor=doc, patient=pat, appt_date=da,status=status_data,temp=patient_data)
 
        return appt

class homeapptserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    #appt_date=date_timeserializer()
    #patient=patientserializer()
    class Meta:
        model=home_appointment
        fields=['id','doctor','appt_date','temp','status']
    def create(self, validated_data):
         doctor_data=validated_data.get('doctor')
         date_time_data = validated_data.pop('appt_date')
         patient_data=validated_data.get('temp')
         status_data=validated_data.get('status')
         if status_data is None:
            status_data="Requested"
         try:
            pat = patient.objects.get(id=patient_data)
         except patient.DoesNotExist:
            pat = patient.objects.create(id=patient_data)
            #pat.save()
         #pat,p= patient.objects.get_or_create(**patient_data)
         print("hello")
         doc = get_object_or_404(doctor, pk=doctor_data.id)
    #     da=date_time.objects.create(**date_time_data)
         appt= home_appointment.objects.create(doctor=doc, appt_date=date_time_data,patient=pat,temp=patient_data,status=status_data)
         return appt