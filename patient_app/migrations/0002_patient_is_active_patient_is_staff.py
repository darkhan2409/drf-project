# Generated by Django 5.0 on 2023-12-10 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]