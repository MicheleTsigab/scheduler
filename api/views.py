from pydoc import doc
from rest_framework.decorators import api_view
from webbrowser import get
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.shortcuts import render

from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h1>Links</h1><ul><li><a href='http://127.0.0.1:8000/admin'>/admin/</a><ul><li>username: michele password: 1234</li></ul></li><h2>Api Links</h2><li><a href='http://127.0.0.1:8000/doctor'>/doctor/</a></li><li>/doctor/{id}/availablity</li><li>/doctor/{id}/homeappt</li><li>/patient/{id}/homeappt</li><li>/doctor/{id}/appt</li><li>/patient/{id}/appt</li></ul></body></html>"
    html+="<h1>For full Documentation<h1> <a href='https://documenter.getpostman.com/view/19708900/UzBgvVM5'>Click here</a>"
    return HttpResponse(html)
@api_view(('GET',))
def setIs_home(request):
    doc=get_object_or_404(doctor,pk=request.GET.get('id'))
    doc.is_home_doctor=request.GET.get('is_home_doctor')
    doc.save()
    return Response(data="ok",status=200)
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
class patapptViewset(viewsets.ModelViewSet):
    serializer_class=apptserializer
    def get_queryset(self):
        return appointment.objects.filter(patient=self.kwargs['patient_pk'])
class dochomeapptViewset(viewsets.ModelViewSet):
    serializer_class=homeapptserializer
    def get_queryset(self):
        return home_appointment.objects.filter(doctor=self.kwargs['doctor_pk'])
class pathomeapptViewset(viewsets.ModelViewSet):
    serializer_class=homeapptserializer
    def get_queryset(self):
        return home_appointment.objects.filter(patient=self.kwargs['patient_pk'])
class doctorsWithinR(viewsets.ReadOnlyModelViewSet):
    serializer_class = doctorserializer
   
    def get_queryset(self):
        longitude = self.request.query_params.get('long')
        latitude= self.request.query_params.get('lat')
        radius = self.request.query_params.get('km')
        location = Point(float(latitude),float(longitude))
        queryset = doctor.objects.filter(location__distance_lt=(location, Distance(km=radius)))
        return queryset



  


