from django.db import models


class Clinic(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.title)
