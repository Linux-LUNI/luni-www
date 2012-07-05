from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'luniSite.views.home', name='home'),
    url(r'^$', 'luniSite.views.Calendar', name='Calendar'),
    url(r'^calendar/', 'luniSite.views.Calendar', name='Calendar'),
    url(r'^mailing/', 'luniSite.views.MailingLists', name='MailingLists'),
    url(r'^orgs/', 'luniSite.views.Organizations', name='Organizations'),
    # url(r'^luniSite/', include('luniSite.foo.urls')),
    #url(r'^calendar/', include('luniCalendar.views.calendar')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
