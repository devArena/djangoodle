from django.conf.urls import patterns, include, url
from djangoodle import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.example, name='example'),
)
