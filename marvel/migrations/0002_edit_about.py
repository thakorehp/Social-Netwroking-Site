# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marvel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edit',
            name='about',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
