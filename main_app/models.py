from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    career_objective = models.TextField(blank=True)
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
    


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('E-commerce', 'E-commerce'),
        ('Blog site', 'Blog site'),
        ('Portfolio site', 'Portfolio site'),
        ('Tutorial site', 'Tutorial site'),
        ('LMS site', 'LMS site'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='main_app/project_images/')
    category = models.CharField(max_length=50, default='default_category', choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

