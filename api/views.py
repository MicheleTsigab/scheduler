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
    serializer_class=apptserializer
    def get_queryset(self):
        return appointment.objects.filter(doctor=self.kwargs['doctor_pk'])
