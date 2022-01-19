# Generated by Django 4.0 on 2022-01-17 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_first_name_alter_user_user_type'),
        ('appointment', '0009_prescription_nurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Nurse',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Nurse', to='account.user'),
            preserve_default=False,
        ),
    ]
