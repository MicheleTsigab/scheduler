# Generated by Django 4.0.3 on 2022-06-17 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_home_appointment_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='temp',
            field=models.CharField(default='2343', max_length=70),
        ),
    ]
