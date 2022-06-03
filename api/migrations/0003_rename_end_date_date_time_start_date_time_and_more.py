# Generated by Django 4.0.3 on 2022-06-02 14:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_patient_lat_alter_patient_long'),
    ]

    operations = [
        migrations.RenameField(
            model_name='date_time',
            old_name='end_date',
            new_name='start_date_time',
        ),
        migrations.RemoveField(
            model_name='date_time',
            name='start_date',
        ),
        migrations.AddField(
            model_name='date_time',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]