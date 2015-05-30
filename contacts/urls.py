__author__ = 'leonardo'
from django.conf.urls import patterns, include, url
from .views import CreateContact, ListContact, ListContactList, ViewContact, CreateSingleContact, EditContact

urlpatterns = patterns('',

    url(r'^create/$', CreateContact.as_view(), name='contact_create'),
    url(r'^create_single/$', CreateSingleContact.as_view(), name='contact_create_single'),
    url(r'^list/$', ListContact.as_view(), name='contact_list'),
    url(r'^list_single/$', ListContactList.as_view(), name='list_contact_list'),
    url(r'^view/(?P<pk>\d+)$', ViewContact.as_view(), name='view_contact'),
    url(r'^edit/(?P<pk>\d+)$', EditContact.as_view(), name='edit_contact'),


)