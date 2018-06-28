from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf.urls.static import static

def dashboard_view(request):
  user = User.objects.get(id=request.session["user_id"])
  if not user.admin:
    return redirect("/products/view/")
  orders = Order.objects.all()
  orderlists = OrderProductList.objects.all()
  context = {
    "user": user,
    "orders": orders,
    "orderlists": orderlists
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
  print(orderlist)
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
  print(request.session["cart"])
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
  order = Order.objects.create(buyer=User.objects.get(id=request.session["user_id"]), status="pending", total=total)
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

