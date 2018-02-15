from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = patterns('',
	url(r'^messages/14/', views.que_14.as_view(), name='que-14'),
	url(r'^messages/15/', views.que_15.as_view(), name='que-15'),
	url(r'^messages/16/', views.que_16.as_view(), name='que-16'),
	url(r'^messages/17/', views.que_17.as_view(), name='que-17'),
	url(r'^messages/18/', views.que_18.as_view(), name='que-18'),
	url(r'^messages/19/', views.que_19.as_view(), name='que-19'),
	url(r'^messages/20/', views.que_20.as_view(), name='que-20'),
)
