# Generated by Django 3.2 on 2022-06-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='labels', to='projects.Label'),
        ),
    ]
