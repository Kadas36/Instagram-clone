# Generated by Django 3.1.5 on 2021-01-19 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0007_auto_20210118_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instagram.image'),
        ),
    ]