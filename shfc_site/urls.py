# from django.conf.urls.defaults import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'shfc_site.views.home', name='home'),
#     # url(r'^shfc_site/', include('shfc_site.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),


# )

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", direct_to_template, {"template": "index.html"}),
    url(r"^archery/", direct_to_template, {"template": "archery/index.html"}),
    url(r"^boats/", direct_to_template, {"template": "boats/index.html"}),
    url(r"^membership/", direct_to_template, {"template": "membership/index.html"}),
    
    url(r"^range/$", 'range.views.index'),
    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),
)
