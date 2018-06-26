from django.conf.urls import url
from . import views
from django.contrib import admin
from apps.index.models import User

# class UserAdmin(admin.ModelAdmin):
#   pass
# admin.site.register(User, UserAdmin)


urlpatterns = [
  url(r'^admin/',admin.site.urls),
  url('^$', views.index),
  url('^register/$', views.register),
  url('^login/$', views.login),
  url('^logout/$', views.logout),
]