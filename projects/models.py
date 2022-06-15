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


@receiver(post_save, sender=Rating)
def update_rating(sender, instance, created, **kwargs):
    if created:
        rating = (instance.design + instance.usability +
                  instance.creativity + instance.content)/4
        instance.rating = + rating
        project = Project.objects.get(id=instance.project.id)
        project.average_rating += rating
        project.content += instance.content
        project.design += instance.design
        project.usability += instance.usability
        project.creativity += instance.creativity
        project.ratings.add(instance)
        project.save()
        instance.save()


class Label(models.Model):
    name = models.CharField(max_length=25)
    projects = models.ManyToManyField(
        Project, related_name="label", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def save_label(cls, instance):
        try:
            label = Label.objects.get(name=instance.name)
            return label

        except instance.DoesNotExist:
            instance.save()
            return instance
