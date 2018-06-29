from django.conf.urls import url
from . import views

urlpatterns = [
  url('^dashboard/view/$', views.dashboard_view, name="add_product"),
  url('^(?P<product_id>\d+)/dashboard/edit_status/$', views.dashboard_edit_product_status),
  url('^(?P<product_id>\d+)/dashboard/edit/$', views.dashboard_edit_product),
  url('^dashboard/add/$', views.dashboard_add_product),
  url('^view/$', views.view),
  url('^(?P<product_id>\d+)/details/$', views.details),
  url('^category/$', views.category),
]