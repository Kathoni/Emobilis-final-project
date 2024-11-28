from django.db import models

# Create your models here.
class Citizen(models.Model):
    image = models.ImageField(upload_to='citizen_images/', blank=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Login(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.name


class Signing(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name
