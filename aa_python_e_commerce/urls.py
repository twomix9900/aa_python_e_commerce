from django.conf.urls import url, include

urlpatterns = [
  url(r'^', include('apps.index.urls')),
  url(r'^orders/', include('apps.orders.urls')),
  url(r'^products/', include('apps.products.urls')),
]