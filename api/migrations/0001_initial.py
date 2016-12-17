# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=datetime.date.today)),
                ('identifier', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SessionSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Session')),
            ],
            options={
                'ordering': ['add_time'],
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='sessionsong',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Song'),
        ),
    ]