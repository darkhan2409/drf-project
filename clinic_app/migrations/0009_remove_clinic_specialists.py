# Generated by Django 5.0 on 2023-12-12 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0008_remove_clinic_reviews_remove_clinic_specialists_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='specialists',
        ),
    ]
