# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlmuser', '0005_wlmuser_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='wlmuser',
            name='twitter_hashtags',
            field=models.CharField(default=b'#DLMChallenge', max_length=254),
        ),
        migrations.AddField(
            model_name='wlmuser',
            name='twitter_prefix',
            field=models.CharField(default='#{number} {title} ({year}):', max_length=254),
        ),
    ]
