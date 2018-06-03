from django.db import models
from django.utils import timezone

# Create your models here.

class Submission(models.Model):
    registration = models.CharField(max_length=8)
    password = models.CharField(max_length=8)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField()

    def __str__(self):
        return self.registration