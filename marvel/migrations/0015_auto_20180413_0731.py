# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-13 07:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0014_auto_20180413_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]