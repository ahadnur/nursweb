from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Program(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:350]

    def __str__(self):
        return self.title


class Python(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:350]

    def __str__(self):
        return self.title
