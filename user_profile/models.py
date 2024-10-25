from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'Profile of {self.user.username}'