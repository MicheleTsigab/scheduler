from pydoc import doc
from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Links</h1><ul><li><a href='http://127.0.0.1:8000/admin'>/admin/</a><ul><li>username: michele password: 1234</li></ul></li><h2>Api Links</h2><li><a href='http://127.0.0.1:8000/doctor'>/doctor/</a></li><li>/doctor/{id}/availablity</li><li>/doctor/{id}/homeappt</li><li>/patient/{id}/homeappt</li><li>/doctor/{id}/appt</li><li>/patient/{id}/appt</li></ul></body></html>"
    return HttpResponse(html)
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
