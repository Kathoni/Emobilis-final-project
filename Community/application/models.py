from django.db import models
from django.contrib.auth.models import User  # You might want to use Django's built-in User model


# Citizen model for registration
class Citizen(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Optional: Use Django's built-in User model for login functionality, or if you need custom fields, keep your Login model


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name