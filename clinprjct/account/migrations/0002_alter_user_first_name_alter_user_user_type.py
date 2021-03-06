# Generated by Django 4.0 on 2022-01-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('D', 'Doctor'), ('P', 'Patient'), ('R', 'Receptionist'), ('HR', 'HR'), ('N', 'Nurse'), ('R', 'Receptionist')], max_length=2),
        ),
    ]
