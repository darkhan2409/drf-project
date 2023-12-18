# Generated by Django 5.0 on 2023-12-11 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0004_remove_clinic_review_clinic_review'),
        ('review_app', '0002_remove_review_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='review',
        ),
        migrations.AddField(
            model_name='clinic',
            name='reviews',
            field=models.ManyToManyField(null=True, to='review_app.review'),
        ),
    ]