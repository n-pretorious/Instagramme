# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-21 06:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instapics', '0002_auto_20190521_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
