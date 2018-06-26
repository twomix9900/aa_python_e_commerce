from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.conf.urls.static import static

def index(request):
  return render(request, "index/index.html")

def login(request):
  if request.method == "POST":
    try:
      result = User.objects.login_validator(request.POST)
      if "success" in result:
        request.session["user_id"] = result["success"].id
        request.session["user_first_name"] = result["success"].first_name
        messages.add_message(request, messages.SUCCESS, 'Log in successful', extra_tags="log_in")
        return redirect("/products/view/")
      else:
        messages.add_message(request, messages.ERROR, 'Invalid login credentials', extra_tags="invalid_login")
        return redirect("/")
    except:
      messages.add_message(request, messages.ERROR, 'Invalid login credentials', extra_tags="invalid_login")
      return redirect("/")
  else:
    return redirect("/")

def register(request):
  if request.method == "POST":
    try:    
      result = User.objects.registration_validator(request.POST)
      if "success" in result:
        request.session["user_id"] = result["success"].id
        request.session["user_first_name"] = result["success"].first_name
        messages.add_message(request, messages.SUCCESS, 'Registration successful', extra_tags="registration")
        return redirect('/products/view/')
      else:
        for key, value in result.items():
          messages.error(request, value, extra_tags=key)
        return redirect('/')
    except:
      pass

  return redirect("/")

def logout(request):
  request.session.clear()
  messages.add_message(request, messages.SUCCESS, 'Logout successful', extra_tags="log_out")
  return redirect("/")