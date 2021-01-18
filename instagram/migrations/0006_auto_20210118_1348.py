# Generated by Django 3.1.5 on 2021-01-18 10:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0005_auto_20210118_1319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.AddField(
            model_name='image',
            name='likes',
            field=models.ManyToManyField(related_name='image_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]