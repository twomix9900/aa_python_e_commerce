from django.contrib import admin
from apps.index.models import User
from apps.orders.models import Order
from apps.products.models import Product
from django.conf.urls import url

class UserAdmin(admin.ModelAdmin):
  pass
admin.site.register(User, UserAdmin)

class OrderAdmin(admin.ModelAdmin):
  pass
admin.site.register(Order, OrderAdmin)

class ProductAdmin(admin.ModelAdmin):
  pass
admin.site.register(Product, ProductAdmin)

urlpatterns = [
  url(r'^admin/',admin.site.urls),
]