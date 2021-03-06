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

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=Project)
    def update_projects(sender, instance, created, **kwargs):
        if created:
            profile = Profile.objects.get(user__id=instance.user.id)
            profile.projects.add(instance)
            profile.save()

    def __str__(self):
        return self.user.username
