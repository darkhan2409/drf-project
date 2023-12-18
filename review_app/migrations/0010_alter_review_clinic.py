# Generated by Django 5.0 on 2023-12-15 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_app', '0010_remove_clinic_reviews'),
        ('review_app', '0009_alter_review_clinic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='clinic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='clinic_app.clinic'),
        ),
    ]
