__author__ = 'leonardogutierrezh'

from django.conf.urls import patterns, include, url
from cases.views import CreateCase, ListCase


urlpatterns = patterns('',

    url(r'^create_case/(?P<pk>\d+)$', CreateCase.as_view(), name='create_case'),
    url(r'^list_case/$', ListCase.as_view(), name='list_case')

)

