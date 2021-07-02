from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=255)

class Role(models.Model):
    name = models.CharField(max_length=255)
    permissions = models.ManyToManyField(Permission)

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.CharField(max_length=255)

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
