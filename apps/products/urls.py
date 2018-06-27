from django.conf.urls import url
from . import views

urlpatterns = [
  url('^dashboard/view/$', views.dashboard_view),
  url('^(?P<product_id>\d+)/dashboard/edit/$', views.dashboard_edit_product),
  url('^view/$', views.view),
  url('^(?P<product_id>\d+)/details/$', views.details),
  url('^cart/(?P<product_id>\d+)/$', views.cart),
  url('^checkout/$', views.checkout),
  url('^category/$', views.category),
]