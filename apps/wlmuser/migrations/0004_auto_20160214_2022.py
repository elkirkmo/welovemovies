# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 20:22
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wlmuser', '0003_auto_20160213_2344'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='wlmuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]