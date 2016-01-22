from django.conf.urls import patterns, include, url

#from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'itmserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^time/$', 'itmserver.views.current_datetime'),
    #url(r'^time/plus/(\d{1,2})/$', 'itmserver.views.hours_ahead'),
    #url(r'^demo/', include('demo.urls')),
    url(r'^autoadmin/', include('autoadmin.urls')),
    url(r'^omaudit/', include('omaudit.urls')),
    url(r'^$','autoadmin.views.index'),


)
