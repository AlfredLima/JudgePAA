from django.db import models
from django.utils import timezone

# Create your models here.

class Submission(models.Model):
    registration = models.CharField(max_length=8)
    date = models.DateTimeField(default=timezone.now)
    file = models.TextField()
    grade = models.IntegerField(default=0)
    evaluation = models.CharField(max_length=200, default='Waiting')

    def __str__(self):
        return str(self.pk)