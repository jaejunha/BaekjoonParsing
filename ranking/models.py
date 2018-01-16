# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    correct = models.IntegerField(default=0, null=True)
    tries = models.IntegerField(default=0, null=True)
    last = models.CharField(max_length=30, default='', null=True)
    status = models.TextField(default='', null=True)
    ds = models.IntegerField(default=0, null=True)
    def __str__(self):
        return self.name

class Problem(models.Model):
    number = models.IntegerField(primary_key=True)