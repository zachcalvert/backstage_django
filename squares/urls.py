from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^difference/$', views.get_difference, name='get_difference'),
]