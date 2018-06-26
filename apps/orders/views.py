from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf.urls.static import static

def dashboard_view(request):
  if request.session["user_id"] == 1:
    return render(request, "orders/dashboard_view.html")
  return redirect("/")

def dashboard_order_details(request, order_id):
  if request.session["user_id"] == 1:
    return render(request, "orders/dashboard_details.html", { "order_id": order_id }) 
  return redirect("/")

# def login(request):
#   if request.method == "POST":
#     try:
#       result = User.objects.login_validator(request.POST)
#       if "success" in result:
#         request.session["user_id"] = result["success"].id
#         request.session["user_first_name"] = result["success"].first_name
#         messages.add_message(request, messages.SUCCESS, 'Log in successful', extra_tags="log_in")
#         return redirect("/orders/view/")
#       else:
#         messages.add_message(request, messages.ERROR, 'Invalid login credentials', extra_tags="invalid_login")
#         return redirect("/")
#     except:
#       messages.add_message(request, messages.ERROR, 'Invalid login credentials', extra_tags="invalid_login")
#       return redirect("/")
#   else:
#     return redirect("/")

# def register(request):
#   if request.method == "POST":
#     try:    
#       result = User.objects.registration_validator(request.POST)
#       if "success" in result:
#         request.session["user_id"] = result["success"].id
#         request.session["user_first_name"] = result["success"].first_name
#         messages.add_message(request, messages.SUCCESS, 'Registration successful', extra_tags="registration")
#         return redirect('/orders/view/')
#       else:
#         for key, value in result.items():
#           messages.error(request, value, extra_tags=key)
#         return redirect('/')
#     except:
#       pass

#   return redirect("/")

# def logout(request):
#   request.session.clear()
#   messages.add_message(request, messages.SUCCESS, 'Logout successful', extra_tags="log_out")
#   return redirect("/")

# def orders(request):
#   if "user_id" not in request.session:
#     return redirect("/")
#   return render(request, "orders/orders.html")

# def add_quote(request):
#   try:    
#     result = Quote.objects.quote_validator(request.POST, request.session["user_id"])
#     if "success" in result:
#       messages.add_message(request, messages.SUCCESS, 'Quote added', extra_tags="update")
#       return redirect('/quotes/')
#     else:
#       for key, value in result.items():
#         messages.error(request, value, extra_tags=key)
#       return redirect('/quotes/')
#   except:
#     pass

#   return redirect("/quotes/")

# def user_details(request, id):
#   context = {
#     "user": User.objects.get(id=id),
#     "quotes": Quote.objects.filter(poster=User.objects.get(id=id)).order_by('-created_at')
#   }
#   return render(request, "index/user_details.html", context)

# def update_user_details(request):
#   return render(request, "index/update_user_details.html", { "user": User.objects.get(id=request.session["user_id"]) })

# def update_user_details_process(request):
#   try:    
#     result = User.objects.update_validator(request.POST, request.session["user_id"])
#     if "success" in result:
#       request.session["user_first_name"] = result["success"].first_name
#       messages.add_message(request, messages.SUCCESS, 'Account information updated', extra_tags="update")
#       return redirect('/quotes/')
#     else:
#       for key, value in result.items():
#         messages.error(request, value, extra_tags=key)
#       print("Patrick is a tamago")
#       return redirect('/user/details/update/')
#   except:
#     pass

#   return redirect("/quotes/")

# def delete_quote(request, quote_id):
#   Quote.objects.get(id=quote_id).delete()
#   return redirect('/quotes/')

# def like_quote(request, quote_id):
#   like = Quote.objects.get(id=quote_id)
#   user = User.objects.get(id=request.session["user_id"])
#   if user not in like.liked_by.all():
#     like.liked_by.add(user)
#     like.save()
#   else:
#     pass
#   return redirect('/quotes/')