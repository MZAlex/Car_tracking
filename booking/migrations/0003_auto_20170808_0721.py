# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 06:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arrival_point',
            name='starting_place',
        ),
        migrations.DeleteModel(
            name='Arrival_point',
        ),
        migrations.DeleteModel(
            name='Starting_point',
        ),
    ]
