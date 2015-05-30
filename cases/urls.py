__author__ = 'leonardogutierrezh'

from django.conf.urls import patterns, include, url
from cases.views import CreateCase, ListCase, ViewCase, MyCases, SendCase, delete_case


urlpatterns = patterns('',

    url(r'^create/(?P<pk>\d+)$', CreateCase.as_view(), name='create_case'),
    url(r'^view/(?P<pk>\d+)$', ViewCase.as_view(), name='view_case'),
    url(r'^delete/(?P<pk>\d+)$', delete_case, name='delete_case'),
    url(r'^list/$', ListCase.as_view(), name='list_case'),
    url(r'^casetrack/list/$', MyCases.as_view(), name='my_cases'),
    url(r'^casetrack/send/(?P<pk>\d+)$', SendCase.as_view(), name='send_case'),

)

