# Generated by Django 4.0 on 2022-01-19 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0010_appointment_nurse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='Nurse',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='Nurse',
        ),
    ]
