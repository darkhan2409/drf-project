from django.db import models
from patient_app.models import Patient
from clinic_app.models import Clinic


class Review(models.Model):
    author = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, related_name='author')
    text = models.TextField()
    created_at = models.DateField(auto_now=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True, related_name='reviews')

    def __str__(self) -> str:
        return str(self.author) + str(' - ') + str(self.created_at)
