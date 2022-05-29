from distutils.command.upload import upload
from statistics import mode
import django
from django.db import models
from django.utils import timezone

# Create your models here.


class Articles(models.Model):
    STATUS_CHOISES = (
        ('d', "Draft"),
        ('p', 'Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES)
