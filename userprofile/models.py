# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserData(models.Model):
      name = models.CharField(max_length=42)
      email = models.EmailField(max_length=75)
      updated_on = models.DateTimeField(auto_now_add=True)
