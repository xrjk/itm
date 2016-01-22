#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('demo.views',
    (r'^$','index'),
)
