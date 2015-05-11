__author__ = 'leonardo'
from django.conf.urls import patterns, include, url
from .views import CreateContact, ListContact

urlpatterns = patterns('',

    url(r'^create/$', CreateContact.as_view(), name='contact_create'),
    url(r'^list/$', ListContact.as_view(), name='contact_list'),

)