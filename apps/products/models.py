from __future__ import unicode_literals
from django.db import models
from apps.orders.models import *

class Product(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  category = models.CharField(max_length=50)
  image = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)
