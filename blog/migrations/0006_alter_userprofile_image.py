# Generated by Django 3.2 on 2023-05-12 14:06

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='default.jpg', storage=django.core.files.storage.FileSystemStorage(location='/home/kali/Desktop/DIAM/FinalProject/sportsblog/bolg/static'), upload_to='profile_pics'),
        ),
    ]
