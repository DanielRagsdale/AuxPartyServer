# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-14 02:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161214_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sessionsong',
            old_name='session_name',
            new_name='session',
        ),
    ]
