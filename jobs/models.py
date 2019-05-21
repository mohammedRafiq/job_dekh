# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
# Create your models here.


class JobsData(models.Model):
      designation = models.CharField(max_length=50,blank=False)
      employer = models.CharField(max_length=100,blank=False)
      years_of_experience = models.CharField(max_length=20,blank=False)
      location = models.CharField(max_length=50)
      title = models.CharField(max_length=200,blank=False)
      description = models.TextField()
      created = models.CharField(max_length=30,default=datetime.now())
