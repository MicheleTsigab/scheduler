# Generated by Django 4.0.3 on 2022-06-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='is_home_doctor',
            field=models.BooleanField(null=True),
        ),
    ]
