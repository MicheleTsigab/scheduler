from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class patient(models.Model):
    patient=models.OneToOneField(User,on_delete=models.CASCADE)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
class doctor(models.Model):
    doctor=models.OneToOneField(User,on_delete=models.CASCADE)
    long = models.DecimalField(max_digits=8, decimal_places=3)
    lat = models.DecimalField(max_digits=8, decimal_places=3)
    availablity=models.ManyToManyField('date_time')
class date_time(models.Model):
    start_date=models.DateField()
    start_time=models.TimeField()
    end_date=models.DateField()
    end_time=models.TimeField()
class schedule(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
class home_schedule(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time, doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(doctor,on_delete=models.CASCADE)

    
