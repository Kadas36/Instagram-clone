# Generated by Django 3.1.5 on 2021-01-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0013_auto_20210119_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpeg', upload_to='profile_pics/'),
        ),
    ]