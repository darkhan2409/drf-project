# Generated by Django 5.0 on 2023-12-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialist_app', '0003_alter_specialist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='experience',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]