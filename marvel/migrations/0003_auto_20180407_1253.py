# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-07 12:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('marvel', '0002_edit_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile', models.ImageField(blank=True, upload_to='Profile_Img')),
                ('Birthdate', models.DateField(blank=True)),
                ('about', models.CharField(blank=True, max_length=2000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='edit',
        ),
    ]
