# Generated by Django 5.0 on 2023-12-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0002_clinic_review'),
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinic',
            name='review',
            field=models.ManyToManyField(blank=True, null=True, to='review_app.review'),
        ),
    ]
