# Generated by Django 3.2 on 2022-06-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0022_auto_20220611_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-posted_at',)},
        ),
    ]