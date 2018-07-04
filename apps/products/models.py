from __future__ import unicode_literals
from django.db import models
from apps.orders.models import *
from django.core.urlresolvers import reverse

class Product(models.Model):
  name = models.CharField(max_length=50)
  desc = models.TextField()
  category = models.CharField(max_length=50)
  image = models.CharField(max_length=255)
  price = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)

  def get_absolute_url(self):
    return reverse("add_product")
  