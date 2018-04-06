# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login,  name='login'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    # url(r'^hcharts/', views.hcharts, name="hcharts"),
    url(r'^dataView/', views.dataView, name="dataView"),
    url(r'^ajaxHcharts/', views.ajaxHcharts, name="ajaxHcharts")
)
