# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Starting_point(models.Model):
    starting_place = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.starting_place

class Arrival_point(models.Model):
    starting_place = models.ForeignKey(Starting_point, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.starting_place
    