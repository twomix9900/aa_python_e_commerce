from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.index.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from .forms import PostForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect


def dashboard_view(request):
  product_list = Product.objects.all()
  page = request.GET.get("page", 1)
  paginator = Paginator(product_list, 10)
  try:
    products = paginator.page(page)
  except PageNotAnInteger:
    products = paginator.page(1)
  except EmptyPage:
    products = paginator.page(paginator.num_pages)
  print(products.paginator)
  context = {
    "products": products,
  }
  return render(request, "products/dashboard_view.html", context)

def dashboard_edit_product_status(request, product_id):
  product = Product.objects.get(id=product_id)
  context = {
    "product": product
  }
  return render(request, "products/dashboard_edit.html", context)

def dashboard_edit_product(request, product_id):
  product = Product.objects.get(id=product_id)
  print(request.POST)
  context = {
    "product": product
  }
  return redirect("/products/dashboard/view/")

def dashboard_add_product(request):
  form = PostForm(request.POST or None, request.FILES or None)
  if form.is_valid():
    instance = form.save(commit=False)
    instance.save()
    messages.success(request, "Successfully created")
    return HttpResponseRedirect(instance.get_absolute_url())

  context = {
    "form": form,
  }
  return render(request, "products/dashboard_add.html", context)

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
  print(products.paginator)
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
    "user": User.objects.get(id=request.session["user_id"]),
    "product": product
  }
  return render(request, "products/details.html", context)

def category(request):
  request.session["category"] = request.GET.get("category", '')
  if request.session["category"] == '':
    del request.session["category"]
  return redirect("/products/view/")