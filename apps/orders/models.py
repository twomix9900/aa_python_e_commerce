from __future__ import unicode_literals
from django.db import models
from apps.index.models import User
from apps.products.models import Product

class Order(models.Model):
  products = models.ManyToManyField(Product, related_name="orders")
  buyer = models.ForeignKey(User, related_name="orders")
  status = models.CharField(max_length=50)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)
