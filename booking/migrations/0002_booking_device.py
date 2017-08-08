# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking_device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(max_length=250)),
                ('arrival_point', models.CharField(max_length=250)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
