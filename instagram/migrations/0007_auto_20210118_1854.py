# Generated by Django 3.1.5 on 2021-01-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0006_auto_20210118_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]