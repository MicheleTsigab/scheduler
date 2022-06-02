from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class patient(models.Model):
    id=models.IntegerField(primary_key=True)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
class doctor(models.Model):
    id=models.IntegerField(primary_key=True)
    long = models.DecimalField(max_digits=16, decimal_places=6)
    lat = models.DecimalField(max_digits=16, decimal_places=6)
    availablity=models.ManyToManyField('date_time',through='doctor_ava')
class doctor_ava(models.Model):
    doctor=models.ForeignKey('doctor',on_delete=models.CASCADE)
    date_time=models.ForeignKey('date_time',on_delete=models.CASCADE)
class date_time(models.Model):
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()  
class appointment(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
class home_appointment(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)

    
