import datetime
from django.shortcuts import get_object_or_404
from .models import *
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
class patientserializer(GeoFeatureModelSerializer):
    class Meta:
        model=patient
        fields=['id','location']
        geo_field = 'location'
class date_timeserializer(serializers.ModelSerializer):
    class Meta:
        model=date_time
        #fields='__all__'
        fields=['date','start_time','end_time']
class doctorserializer(GeoFeatureModelSerializer):
   # availablity=dateserializer()
    class Meta:
        model=doctor
        fields=['id','location']
        geo_field = 'location'
class doctoravaserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    date_time=date_timeserializer()
    class Meta:
        model=doctor_ava
        fields=['id','doctor','date_time']
    
    def create(self, validated_data):
        doctor_data=validated_data.get('doctor')
        date_time_data = validated_data.pop('date_time')
        a = get_object_or_404(doctor, pk=doctor_data.id)
        da=date_time.objects.create(**date_time_data)
        doctor_availablity= doctor_ava.objects.create(doctor=a, date_time=da)
        return doctor_availablity

class apptserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    appt_date=date_timeserializer()
    
    class Meta:
        model=appointment
        fields=['id','doctor','appt_date','status','patient']
    def create(self, validated_data):
        doctor_data=validated_data.get('doctor')
        date_time_data = validated_data.pop('appt_date')
        patient_data=validated_data.get('patient')
        status_data=validated_data.get('status')
        pat= get_object_or_404(patient, pk=patient_data.id)
        doc = get_object_or_404(doctor, pk=doctor_data.id)
        da=date_time.objects.create(**date_time_data)
        appt= appointment.objects.create(doctor=doc, appt_date=da,patient=pat,status=status_data)
        return appt

class homeapptserializer(WritableNestedModelSerializer,serializers.ModelSerializer):
    appt_date=date_timeserializer()
   # patient=patientserializer()
    class Meta:
        model=home_appointment
        fields=['id','doctor','appt_date','status','patient']
    def create(self, validated_data):
        doctor_data=validated_data.get('doctor')
        date_time_data = validated_data.pop('appt_date')
        patient_data=validated_data.get('patient')
        status_data=validated_data.get('status')
        pat= get_object_or_404(patient, pk=patient_data.id)
        doc = get_object_or_404(doctor, pk=doctor_data.id)
        da=date_time.objects.create(**date_time_data)
        appt= home_appointment.objects.create(doctor=doc, appt_date=da,patient=pat,status=status_data)
        return appt