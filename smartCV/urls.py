from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^smartCVApp$', 'smartCV.smartCVApp.views.home', name='home'),
     url(r'^smartCVApp/start$', 'smartCV.smartCVApp.views.start_session', name='start_session'),
     url(r'^smartCVApp/grant$', 'smartCV.smartCVApp.views.grant_session', name='grant_session'),
     url(r'^smartCVApp/get_profile$', 'smartCV.smartCVApp.views.start_granted_session_data', name='start_granted_session_data'),
    # url(r'^smartCV/', include('smartCV.foo.urls')),
    # url(r'^smartCV/', include('smartCV.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
