from django.conf.urls import patterns, include, url

import views

urlpatterns = [
    url(r'^difference/$', views.get_difference, name='get_difference'),
]