from django.contrib import admin
from projects.models import Project, Rating, Label
admin.site.register(Project)
admin.site.register(Rating)
admin.site.register(Label)
