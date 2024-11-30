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
class Login(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Optional: You may not need this if it's just a repeat of Login, so consider merging or clarifying its role
class Signing(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Crime Report model linked to Citizen
class CrimeReport(models.Model):
    user = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)  # This could be a location name or coordinates
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.user.name} at {self.location}"

# Blog Post model
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

    def get_excerpt(self):
        return self.content[:100]

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return self.name