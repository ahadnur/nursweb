from django.db import models
from datetime import datetime


class Problem(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    problem_setter = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:250]
