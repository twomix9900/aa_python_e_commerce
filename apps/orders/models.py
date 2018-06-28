from __future__ import unicode_literals
from django.db import models
from apps.index.models import User
from apps.products.models import Product

class Order(models.Model):
  products = models.ManyToManyField(Product, related_name="orders", blank=True)
  buyer = models.ForeignKey(User, related_name="orders")
  status = models.CharField(max_length=50)
  total = models.IntegerField(default=1)
  shipping_first_name = models.CharField(max_length=50, default="")
  shipping_last_name = models.CharField(max_length=50, default="")
  billing_first_name = models.CharField(max_length=50, default="")
  billing_last_name = models.CharField(max_length=50, default="")
  shipping_address_1 = models.TextField(default="")
  billing_address_1 = models.TextField(default="")
  shipping_address_2 = models.TextField(blank=True, default="")
  billing_address_2 = models.TextField(blank=True, default="")
  shipping_city = models.TextField(default="")
  billing_city = models.TextField(default="")
  shipping_state = models.CharField(max_length=2, default="")
  billing_state = models.CharField(max_length=2, default="")
  shipping_zip = models.IntegerField(null=True)
  billing_zip = models.IntegerField(null=True)
  cc_number = models.IntegerField(null=True)
  cc_security_code = models.IntegerField(null=True)
  cc_exp_month = models.IntegerField(null=True)
  cc_exp_year = models.IntegerField(null=True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)

class OrderProductList(models.Model):
  order = models.ForeignKey(Order, related_name="list_orders")
  product = models.ForeignKey(Product, related_name="list_orders")
  quantity = models.IntegerField(default=1)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now_add = True)