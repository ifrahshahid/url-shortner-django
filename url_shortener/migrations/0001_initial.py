# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 09:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alias', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(max_length=2083)),
                ('click_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
