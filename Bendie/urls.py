from django.urls import path, include
from django.conf.urls import url
from . import views
from Bendie import views as bendie_views

urlpatterns = [
     url(r'^$', views.index, name='index'),
       url(r'^devices/(?P<id_room>[-A-Za-z0-9_]+)$', bendie_views.devices, name='devices'),
]  

urlpatterns += [
    path('', include('django.contrib.auth.urls')),
]     