# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class booking_device(models.Model):
    starting_point = models.CharField(max_length=250)
    arrival_point = models.CharField(max_length=250)
    
    def __str__(self):
        return self.starting_point