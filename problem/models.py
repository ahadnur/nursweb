from django.db import models
from datetime import datetime
from myblog.utils import unique_slug_generator
from django.db.models.signals import pre_save


class Problem(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    body = models.TextField()
    problem_setter = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    def body_preview(self):
        return self.body[:250]


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Problem)