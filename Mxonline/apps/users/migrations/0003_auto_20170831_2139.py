# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-08-31 13:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_banner_emailverifyrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birday',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now, verbose_name='\u751f\u65e5'),
        ),
    ]