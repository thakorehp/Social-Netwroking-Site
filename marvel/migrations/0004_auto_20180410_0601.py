# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-10 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0003_auto_20180407_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_profile',
            field=models.ImageField(blank=True, upload_to='/media/Profil_Img/'),
        ),
    ]
