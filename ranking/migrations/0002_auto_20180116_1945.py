# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='tries',
            field=models.IntegerField(default=0),
        ),
    ]
