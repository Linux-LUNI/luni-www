from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'luniSite.views.Home', name='Home'),
    url(r'^calendar/', 'luniSite.views.Calendar', name='Calendar'),
    url(r'^contactus/', 'luniSite.views.ContactUs', name='ContactUs'),
    url(r'^orgs/', 'luniSite.views.Organizations', name='Organizations'),
    url(r'^news/', 'newsfeed.views.main', name='news'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ##Apparently the 3 next lines are a bad idea and should only be used for devel.  Though
    ## since I'm deploying on heroku, I'm not sure how to serve these files statically without
    ## moving out of the heroku environment.
    (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/img'}),
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/css'}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'static/js'}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
