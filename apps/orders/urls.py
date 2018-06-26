from django.conf.urls import url
from . import views

urlpatterns = [
  url('^dashboard/view/$', views.dashboard_view),
  url('^dashboard/(?P<order_id>\d+)/details/$', views.dashboard_order_details),
]