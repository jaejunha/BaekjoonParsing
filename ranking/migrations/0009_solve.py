# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0008_problem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
