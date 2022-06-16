#import datetime
#from django.utils.timezone import utc
from django.db import models
from django.contrib.gis.db import models
#from django.contrib.auth.models import User
# Create your models here.
class patient(models.Model):
    id=models.CharField(primary_key=True,max_length=70)
    #long = models.DecimalField(max_digits=16, decimal_places=6)
    location = models.PointField()
    appt=models.ManyToManyField('doctor',through='appointment')
class doctor(models.Model):
    id=models.CharField(primary_key=True,max_length=70)
    location = models.PointField()
    #availablity=models.ManyToManyField('date_time',through='doctor_ava')
    home_appt=models.ManyToManyField('patient',through='home_appointment')
class doctor_ava(models.Model):
    #class meta:
       # constraints =[ models.UniqueConstraint(fields = ['days', 'start_time','end_time'], name = 'constraint_name')]
    CHOICES = [(i,i) for i in range(1,8)]
    doctor=models.ForeignKey('doctor',on_delete=models.CASCADE)
    days = models.IntegerField(choices=CHOICES)
    start_time=models.TimeField()
    end_time=models.TimeField()
    #date_time=models.ForeignKey('date_time',on_delete=models.CASCADE)
class date_time(models.Model):
    class meta:
       constraints =[ models.UniqueConstraint(fields = ['date','start_time','end_time'], name = 'date_constraint')]
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField() 
    def get_duration(self):
        return self.start_time - self.end_time
        
class appointment(models.Model):
    class meta:
       constraints =[ models.UniqueConstraint(fields = ['doctor','appt_date'], name = 'appointment_constraint')]
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,null=True)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
class home_appointment(models.Model):
    doctor=models.ForeignKey(doctor,on_delete=models.CASCADE)
    appt_date=models.ForeignKey(date_time,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,null=True)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)

    
