# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 06:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welovemovies', '0006_auto_20160214_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewing',
            name='how_watched',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
