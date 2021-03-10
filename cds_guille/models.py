# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings


class Album(models.Model):
    title = models.CharField(max_length=500)
    year = models.IntegerField(blank=True, null=True)
    artist = models.ForeignKey('Band', on_delete=models.CASCADE)
    original = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ('year',)

class Band(models.Model):
    name = models.CharField(max_length=500)
