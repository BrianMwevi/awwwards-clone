# Generated by Django 3.2 on 2022-06-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0019_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
