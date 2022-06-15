from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Project(models.Model):
    user = models.ForeignKey(
        User, related_name='author', on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    ratings = models.ManyToManyField(
        'Rating', related_name='user_ratings', blank=True)
    design = models.PositiveBigIntegerField(blank=True, default=0)
    creativity = models.PositiveBigIntegerField(blank=True, default=0)
    content = models.PositiveBigIntegerField(blank=True, default=0)
    usability = models.PositiveBigIntegerField(blank=True, default=0)
    average_rating = models.PositiveBigIntegerField(
        blank=True, default=0)
    labels = models.ManyToManyField(
        "Label", related_name="project", blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-posted_at',)

    def __str__(self):
        return self.name


class Rating(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    design = models.PositiveIntegerField(default=0)
    usability = models.PositiveIntegerField(default=0)
    creativity = models.PositiveIntegerField(default=0)
    content = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0, blank=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.rating}"
