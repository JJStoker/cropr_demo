from django.conf.urls import url

from croplet_demo.croplet.views import authorize
from views import Home, MapView, callback

urlpatterns = [
    url(r'^$', Home.as_view(), name="home"),
    url(r'map/$', MapView.as_view(), name="map"),
    url(r'authorize/$', authorize, name="authorize"),
    url(r'callback/$', callback, name="callback"),
]