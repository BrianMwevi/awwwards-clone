# Generated by Django 3.2 on 2022-06-11 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
