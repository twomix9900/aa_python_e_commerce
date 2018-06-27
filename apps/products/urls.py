from django.conf.urls import url
from . import views

urlpatterns = [
  url('^dashboard/view/$', views.dashboard_view),
  url('^(?P<product_id>\d+)/dashboard/edit/$', views.dashboard_edit_product),
  url('^view/$', views.view),
  url('^(?P<product_id>\d+)/details/$', views.details),
  url('^cart/$', views.cart),
  url('^cartprocess/(?P<product_id>\d+)/$', views.cartprocess),
  url('^checkout/$', views.checkout),
  url('^category/$', views.category),
  url('^cart/delete/$', views.delete_cart_item),
]