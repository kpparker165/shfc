from django.conf.urls import url

from . import views

app_name = 'shfc'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^range/$', views.range, name='range'),
    url(r'^marine/$', views.marine, name='marine'),
    url(r'^membership/$', views.membership, name='membership'),
    url(r'^save/$', views.save, name='save'),
    url(r'^purchase/$', views.purchase, name='purchase'),
    url(r'^calendar/$', views.calendar, name='calendar'),
    url(r'^newAnnouncement/$', views.newAnnouncement, name='newAnnouncement'),
    url(r'^updateHomePage/$', views.updateHomePage, name='updateHomePage'),
    url(r'^updateRSOCalendar/$', views.updateRSOCalendar, name='updateRSOCalendar'),

]