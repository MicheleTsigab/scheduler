# Generated by Django 4.0.3 on 2022-06-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_home_appointment_appt_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='location',
        ),
        migrations.AlterField(
            model_name='home_appointment',
            name='status',
            field=models.CharField(default='Requested', max_length=50),
        ),
    ]
