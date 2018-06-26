from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.index.models import *
from django.contrib import messages
from django.conf.urls.static import static
from django.core.paginator import Paginator

def dashboard_view(request):
  return render(request, "products/dashboard_view.html")

def dashboard_edit_product(request, product_id):
  return render(request, "products/dashboard_edit.html", { 'product_id': product_id })

def view(request):
  context = {
    "admin": User.objects.get(id=request.session["user_id"]).admin,
    "products": Product.objects.all()
  }
  return render(request, "products/view.html", context)

def details(request, product_id):
  return render(request, "products/details.html", { 'product_id': product_id })

def cart(request):
  return render(request, "products/cart.html")

def checkout(request):
  return render(request, "products/checkout.html")