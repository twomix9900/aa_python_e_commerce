from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf.urls.static import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def dashboard_view(request):
  user = User.objects.get(id=request.session["user_id"])
  if not user.admin:
    return redirect("/products/view/")
  order_list = Order.objects.all()
  page = request.GET.get("page", 1)
  paginator = Paginator(order_list, 5)
  try:
    orders = paginator.page(page)
  except PageNotAnInteger:
    orders = paginator.page(1)
  except EmptyPage:
    orders = paginator.page(paginator.num_pages)
  orderlists = OrderProductList.objects.all()
  context = {
    "user": user,
    "orders": orders,
    "orderlists": orderlists,
    "select_options": ["Shipped", "Order in process", "Cancelled"]
  }
  return render(request, "orders/dashboard_view.html", context)

def dashboard_order_details(request, order_id):
  user = User.objects.get(id=request.session["user_id"])
  if not user.admin:
    return redirect("/products/view/")
  order = Order.objects.get(id=order_id)
  orderlist = OrderProductList.objects.filter(order=order)
  context = {
    "user": user,
    "order_id": order_id,
    "order": order,
    "orderlist": orderlist,
  }
  return render(request, "orders/dashboard_details.html", context)

def checkout(request):
  order = Order.objects.get(id=request.session["order_id"])
  context = {
    "user": User.objects.get(id=request.session["user_id"]),
    "order": order,
    "orderlist": OrderProductList.objects.filter(order=order)
  }
  return render(request, "orders/checkout.html", context)

def checkoutprocess(request):
  temp_cart = []
  for item in request.session["cart"]:
    temp = Product.objects.get(id = item["id"])
    temp.quantity = item["quantity"]
    temp.total = item["total"]
    temp.save()
    temp_cart.append(temp)
  Orders.objects.create()
  return redirect("/orders/checkout/")

def cartprocess(request, product_id):
  if "cart" not in request.session:
    request.session["cart"] = []
  product = Product.objects.get(id=product_id)
  item = {
    'id': product.id,
    'name': product.name,
    'quantity': request.POST["quantity"],
    'price': product.price,
    'total': product.price * int(request.POST["quantity"])
  }
  request.session["cart"].append(item)
  request.session["cart_count"] += int(request.POST["quantity"])
  request.session.modified = True
  return redirect("/orders/cart/")

def delete_cart_item(request):
  product = request.GET.get("product","")
  idx = None
  for i in range(len(request.session["cart"])):
    if request.session["cart"][i]["name"] == product:
      idx = i
      request.session["cart_count"] -= int(request.session["cart"][i]["quantity"])
      break
  if idx != None:
    request.session["cart"].pop(idx)
    request.session.modified = True
  return redirect("/orders/cart/")

def cart(request):
  total = 0
  if "cart" in request.session:
    for item in request.session["cart"]:
      total += item["total"]

  context = {
    "user": User.objects.get(id=request.session["user_id"]),
    "total": total,
  }
  return render(request, "orders/cart.html", context)

def checkoutprocess(request):
  total = request.GET.get("total",0)
  quantities = []
  order = Order.objects.create(buyer=User.objects.get(id=request.session["user_id"]), total=total, shipping_first_name=request.POST["shipping_first_name"], billing_first_name=request.POST["billing_first_name"], shipping_last_name=request.POST["shipping_last_name"], billing_last_name=request.POST["billing_last_name"], shipping_address_1=request.POST["shipping_address_1"], billing_address_1=request.POST["billing_address_1"], shipping_address_2=request.POST["shipping_address_2"], billing_address_2=request.POST["billing_address_2"], shipping_city=request.POST["shipping_city"], billing_city=request.POST["billing_city"], shipping_state=request.POST["shipping_state"], billing_state=request.POST["billing_state"], shipping_zip=request.POST["shipping_zip"], billing_zip=request.POST["billing_zip"], cc_number=request.POST["cc_number"], cc_security_code=request.POST["cc_security_code"], cc_exp_month=request.POST["cc_exp_month"], cc_exp_year=request.POST["cc_exp_year"])
  for item in request.session["cart"]:
    order.products.add(Product.objects.get(id=item["id"]))
    quantities.append(item["quantity"])
  order.save()
  for i in range(len(order.products.all())):
    OrderProductList.objects.create(order=order, product=order.products.all()[i], quantity=quantities[i])
  request.session["order_id"] = order.id
  request.session["cart_count"] = 0
  del request.session["cart"]
  return redirect("/orders/checkout/")

def dashboard_edit_order(request, order_id):
  order = Order.objects.get(id=order_id)
  order.status = request.POST["status"]
  order.save()
  return redirect("/orders/dashboard/view/")