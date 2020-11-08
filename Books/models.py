from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    pdf = models.FileField(upload_to="books/images",max_length=100)

    def __str__(self):
        return self.title
