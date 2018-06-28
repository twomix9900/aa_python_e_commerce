from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.index.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count


def dashboard_view(request):
  return render(request, "products/dashboard_view.html")

def dashboard_edit_product(request, product_id):
  return render(request, "products/dashboard_edit.html", { 'product_id': product_id })

def view(request):
  if "category" not in request.session:
    product_list = Product.objects.all()
  else:
    product_list = Product.objects.filter(category=request.session["category"])
  page = request.GET.get("page", 1)
  paginator = Paginator(product_list, 10)
  try:
    products = paginator.page(page)
  except PageNotAnInteger:
    products = paginator.page(1)
  except EmptyPage:
    products = paginator.page(paginator.num_pages)

  context = {
    "user": User.objects.get(id=request.session["user_id"]),
    "all_products": Product.objects.all(),
    "products": products,
    "product_categories": Product.objects.values('category').annotate(count=Count('category')),
  }
  return render(request, "products/view.html", context)

def details(request, product_id):
  product = Product.objects.get(id=product_id)
  temp = product.price
  product.price = temp

  context = {
    "product": product
  }
  return render(request, "products/details.html", context)

def category(request):
  request.session["category"] = request.GET.get("category", '')
  if request.session["category"] == '':
    del request.session["category"]
  return redirect("/products/view/")