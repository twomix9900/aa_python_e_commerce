from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^', include('apps.index.urls')),
  url(r'^orders/', include('apps.orders.urls')),
  url(r'^products/', include('apps.products.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)