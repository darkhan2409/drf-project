# Generated by Django 5.0 on 2023-12-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialist_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialist',
            name='clinic',
        ),
    ]