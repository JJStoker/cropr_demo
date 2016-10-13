from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login

from croplet.models import AccessToken

admin.autodiscover()
admin.site.register(AccessToken)

urlpatterns = [
    url(r'^', include('croplet_demo.croplet.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
