from django.db import models
from django.utils import timezone


class Submission(models.Model):
    name = models.CharField(max_length=100)
    registration = models.CharField(max_length=8)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='codes/')
    grade = models.IntegerField(default=0)
    evaluation = models.CharField(max_length=200, default='Avaliando')

    def __str__(self):
        return str(self.pk)