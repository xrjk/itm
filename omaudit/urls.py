#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url


urlpatterns = patterns('omaudit.views',
    (r'^$','index'),
    (r'omaudit_pull/$','omaudit_pull'),
    (r'omaudit_run/$','omaudit_run'),
)
