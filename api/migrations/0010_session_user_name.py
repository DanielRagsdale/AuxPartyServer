# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 23:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='user_name',
            field=models.CharField(default='test', max_length=250),
            preserve_default=False,
        ),
    ]
