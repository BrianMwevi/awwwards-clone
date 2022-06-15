from email.mime import image
from email.policy import default
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from projects.models import Project


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    is_jury = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default="profile.png")

 
           
    def __str__(self):
        return self.user.username
