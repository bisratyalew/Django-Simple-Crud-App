# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'profile_image'),
        ),
    ]