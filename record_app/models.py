from django.db import models
from clinic_app.models import Clinic
from specialist_app.models import Specialist
from patient_app.models import Patient


class Record(models.Model):

    name = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    date = models.DateField(auto_created=False)
    time = models.TimeField(auto_created=False)

    def __str__(self) -> str:
        return str(self.clinic) + str(' - ') + str(self.date)


