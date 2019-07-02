from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.CharField(max_length=100)
    post_time = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:500]

    def __str__(self):
        return self.title
