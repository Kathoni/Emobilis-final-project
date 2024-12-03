from django.db import models
from django.contrib.auth.models import User  # You might want to use Django's built-in User model


# Citizen model for registration
class Citizen(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Optional: Use Django's built-in User model for login functionality, or if you need custom fields, keep your Login model


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    message = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    post = models.TextField()
    def __str__(self):
        return self.name
