from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from myblog.utils import unique_slug_generator
from django.db.models.signals import pre_save



class Program(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:350]

    def __str__(self):
        return self.title

# def slug_generator(sender, instance, *args, **kwargs):
#     if not instance.slug:
#         instance.slug = unique_slug_generator(instance)
# pre_save.connect(slug_generator, sender=Program)



class Python(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)

    def body_preview(self):
        return self.body[:350]

    def __str__(self):
        return self.title

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(slug_generator, sender=Python)
