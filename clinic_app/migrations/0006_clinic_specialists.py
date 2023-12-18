# Generated by Django 5.0 on 2023-12-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0005_remove_clinic_review_clinic_reviews'),
        ('specialist_app', '0002_remove_specialist_clinic'),
    ]

    operations = [
        migrations.AddField(
            model_name='clinic',
            name='specialists',
            field=models.ManyToManyField(null=True, to='specialist_app.specialist'),
        ),
    ]
