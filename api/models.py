#import datetime
#from django.utils.timezone import utc
from django.db import models

#from django.contrib.auth.models import User
# Create your models here.
class patient(models.Model):
    id=models.IntegerField(primary_key=True)
    long = models.DecimalField(max_digits=16, decimal_places=6)
    lat = models.DecimalField(max_digits=16, decimal_places=6)
    appt=models.ManyToManyField('doctor',through='appointment')
class doctor(models.Model):
    id=models.IntegerField(primary_key=True)
    long = models.DecimalField(max_digits=16, decimal_places=6)
    lat = models.DecimalField(max_digits=16, decimal_places=6)
    availablity=models.ManyToManyField('date_time',through='doctor_ava')
    home_appt=models.ManyToManyField('patient',through='home_appointment')
class doctor_ava(models.Model):
    doctor=models.ForeignKey('doctor',on_delete=models.CASCADE)
    date_time=models.ForeignKey('date_time',on_delete=models.CASCADE)
class date_time(models.Model):
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField() 
    def get_duration(self):
        return self.start_time - self.end_time
        
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

    
