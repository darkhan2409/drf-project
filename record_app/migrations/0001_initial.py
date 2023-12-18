# Generated by Django 5.0 on 2023-12-11 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic_app', '0005_remove_clinic_review_clinic_reviews'),
        ('specialist_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TextField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic_app.clinic')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('specialist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specialist_app.specialist')),
            ],
        ),
    ]
