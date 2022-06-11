from distutils.command.upload import upload
from email.policy import default
from operator import mod
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from turtle import position
import django
from django.db import models
from django.forms import BooleanField
from django.utils import timezone
from extentions.utils import jalali_converter

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی‌ها"

    def __str__(self):
        return self.title


class Article(models.Model):
    STATUS_CHOISES = (
        ('d', "پیش‌نویس"),
        ('p', 'منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    description = models.TextField(verbose_name="متن مقاله")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    publish = models.DateTimeField(
        default=timezone.now, verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOISES, verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = "زمان انتشار"
