# Generated by Django 3.1.5 on 2021-01-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_auto_20210118_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
