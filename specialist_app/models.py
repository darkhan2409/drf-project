from django.db import models
from clinic_app.models import Clinic


class Specialist(models.Model):
    SPECIALITY_TYPES = (
        ('Therapist', 'Therapist'),
        ('Surgeon', 'Surgeon'),
        ('Pediatrician', 'Pediatrician'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Neurologist', 'Neurologist'),
        ('Dentist', 'Dentist'),
        ('Oncologist', 'Oncologist')
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    speciality = models.CharField(max_length=20, choices=SPECIALITY_TYPES)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, related_name='specialists')
    experience = models.IntegerField(max_length=2, blank=True, null=True)
    price = models.CharField(max_length=7)

    def __str__(self) -> str:
        return str(self.speciality)


