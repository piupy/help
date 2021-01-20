from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=15,default='')
    email = models.CharField(max_length=100, default='')
    content = models.TextField(default='')
    timestamp = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,default='')
    content = models.TextField(default='')
    author = models.CharField(max_length=50, default='')
    slug = models.CharField(max_length=100, default='')
    timestamp = models.DateTimeField(blank=True)


    def __str__(self):
        return self.title + ' by ' + self.author


