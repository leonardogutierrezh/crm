from django.conf.urls import patterns, include, url
from django.contrib import admin
from cases.views import login, logout, auth_view

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login),
    url(r'^auth/$', auth_view),
    url(r'logout/$', logout, name='logout'),
    url(r'^case/', include('cases.urls')),
    url(r'^contact/', include('contacts.urls')),
)
