from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.
class doctorViewset(viewsets.ModelViewSet):
    serializer_class = doctorserializer
    queryset = doctor.objects.all()
class patientViewset(viewsets.ModelViewSet):
    serializer_class = patientserializer
    queryset = patient.objects.all()
class availablityViewset(viewsets.ModelViewSet):
    serializer_class=doctoravaserializer
    def get_queryset(self):
        return doctor_ava.objects.filter(doctor=self.kwargs['doctor_pk'])
class docapptViewset(viewsets.ModelViewSet):
    serializer_class=docapptserializer
    def get_queryset(self):
        return appointment.objects.filter(doctor=self.kwargs['doctor_pk'])
class patapptViewset(viewsets.ModelViewSet):
    serializer_class=patapptserializer
    def get_queryset(self):
        return appointment.objects.filter(patient=self.kwargs['patient_pk'])
class dochomeapptViewset(viewsets.ModelViewSet):
    serializer_class=dochomeapptserializer
    def get_queryset(self):
        return home_appointment.objects.filter(doctor=self.kwargs['doctor_pk'])
class pathomeapptViewset(viewsets.ModelViewSet):
    serializer_class=pathomeapptserializer
    def get_queryset(self):
        return home_appointment.objects.filter(doctor=self.kwargs['doctor_pk'])
