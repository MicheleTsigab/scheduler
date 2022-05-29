from .models import *
from rest_framework import serializers
class patientserializer(serializers.ModelSerializer):
    class Meta:
        model=patient
        fields='__all__'
class dateserializer(serializers.ModelSerializer):
    class Meta:
        model=date_time
        fields='__all__'
class doctorserializer(serializers.ModelSerializer):
    availability=dateserializer()
    class Meta:
        model=doctor
        fields=['doctor','availability']
class apptserializer(serializers.ModelSerializer):
    class Meta:
        model=appointment
        fields=['appt_date','status']
class homeapptserializer(serializers.ModelSerializer):
    class Meta:
        model=home_appointment
        fields=['appt_date','status']
