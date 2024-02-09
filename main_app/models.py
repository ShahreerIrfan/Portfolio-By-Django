# main_app/models.py

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    career_objective = models.TextField(blank=True)
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
