# Generated by Django 3.2 on 2022-06-10 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='average_rating',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]