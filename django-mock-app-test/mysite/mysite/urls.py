
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
            url(r'^referees/', include('referees.urls')),
                url(r'^admin/', include(admin.site.urls)),
                ]
