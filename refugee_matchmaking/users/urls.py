from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('',
	url(r'^$', views.add_user, name="index"),
	url(r'^user/(?P<pk>[0-9a-z]+)/$', views.user_detail, name='user_detail'),
)