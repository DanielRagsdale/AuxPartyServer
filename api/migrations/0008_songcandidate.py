# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-15 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_songrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongCandidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_session', to='api.Session')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_songs', to='api.Song')),
            ],
        ),
    ]