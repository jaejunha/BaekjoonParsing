# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0006_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ds',
            field=models.IntegerField(default=0, null=True),
        ),
    ]