# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-16 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0005_user_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]