from django.conf.urls import patterns, include, url
from project3.views import hello, current_datetime, hours_ahead, hours_behind

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project3.views.home', name='home'),
    # url(r'^project3/', include('project3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead), 
    (r'^time/minus/(\d{1,2})/$', hours_behind),
)

