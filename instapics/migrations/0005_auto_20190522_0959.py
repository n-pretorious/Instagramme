# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-22 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instapics', '0004_auto_20190522_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['first_name']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
    ]
