from django.db import models
from datetime import datetime
from myblog.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    body = models.TextField()
    author = models.CharField(max_length=100)
    post_time = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:350]

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)