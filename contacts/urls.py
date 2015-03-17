__author__ = 'leonardo'
from django.conf.urls import patterns, include, url
from .views import CreateContact, ListContact

urlpatterns = patterns('',

    url(r'^create_contact/$', CreateContact.as_view(), name='contact_create'),
    url(r'^list_contact/$', ListContact.as_view(), name='contact_list'),

)