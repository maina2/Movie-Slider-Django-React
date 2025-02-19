from django.db import models
from django.contrib.auth.models import AbstractUser
import cloudinary.models

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=100, blank=True, null=True)
    profile_picture = cloudinary.models.CloudinaryField('image', blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username
