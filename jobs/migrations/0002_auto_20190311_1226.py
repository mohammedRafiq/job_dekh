# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-11 12:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsdata',
            name='created_at',
            field=models.DateTimeField(max_length=100, verbose_name=datetime.datetime(2019, 3, 11, 12, 26, 38, 109449)),
        ),
    ]