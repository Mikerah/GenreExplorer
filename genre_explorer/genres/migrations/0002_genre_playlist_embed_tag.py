# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='playlist_embed_tag',
            field=models.CharField(default='', max_length=250),
        ),
    ]
