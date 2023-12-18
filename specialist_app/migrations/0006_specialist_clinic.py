# Generated by Django 5.0 on 2023-12-12 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0009_remove_clinic_specialists'),
        ('specialist_app', '0005_alter_specialist_speciality'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='clinic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic_app.clinic'),
        ),
    ]
