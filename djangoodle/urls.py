from django.conf.urls import patterns, include, url
from djangoodle import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.main, name='main'),
    url(r'^event/$', views.event, name='event'),
    url(r'^event/(?P<event_id>\S+)/$', views.event_detail, name='event_detail'),
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^add_participant/$', views.add_participant, name='add_participant'),
    url(r'^get_participants/(?P<event_id>\S+)/', views.get_participants, name='get_participants'),
    url(r'^delete_participant/$', views.delete_participant, name='delete_participant'),
    url(r'^edit_participant/$', views.edit_participant, name='edit_participant'),
    )
