from django.conf.urls import patterns, include, url
from djangoodle import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^event/$', views.event, name='event'),
    url(r'^event/(?P<event_id>\d+)/$', views.event_detail, name='event_detail'),
    url(r'^create_event/$', views.create_event, name='create_event'),
    )