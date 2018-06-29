from django.conf.urls import url
from . import views

urlpatterns = [
  url('^dashboard/view/$', views.dashboard_view),
  url('^dashboard/(?P<order_id>\d+)/details/$', views.dashboard_order_details),
  url('^checkout/$', views.checkout),
  url('^checkoutprocess/$', views.checkoutprocess),
  url('^cart/delete/$', views.delete_cart_item),
  url('^cart/$', views.cart),
  url('^cartprocess/(?P<product_id>\d+)/$', views.cartprocess),
  url('^dashboard/(?P<order_id>\d+)/edit/$', views.dashboard_edit_order),
]