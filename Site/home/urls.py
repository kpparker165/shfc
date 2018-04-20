from django.conf.urls import url

from . import views

app_name = 'shfc'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),

    # Range

    url(r'^range/$', views.range, name='range'),
    url(r'^range/shooting/$', views.rangeShooting, name='rangeShooting'),
    url(r'^range/archery/$', views.rangeArchery, name='rangeArchery'),
    url(r'^range/images/$', views.rangeImages, name='rangeImages'),

    # Marine
    url(r'^marine/$', views.marine, name='marine'),
    url(r'^marine/boats_rentals_information/$', views.marineBoatInformation, name='marineBoatInformation'),
    url(r'^marine/trips/$', views.marineBoatTrips, name='marineBoatTrips'),

    url(r'^membership/$', views.membership, name='membership'),
    url(r'^save/$', views.save, name='save'),

    # Purchasing
    url(r'^purchase/$', views.purchase, name='purchase'),
    url(r'^purchase/powder_valley/$', views.purchasePowderValley, name='purchasePowderValley'),

    # Events and classes
    url(r'^events/$', views.events, name='events'),
    url(r'^events/classes/$', views.eventsClasses, name='eventsClasses'),
    url(r'^documents/$', views.documents, name='documents'),


    url(r'^updateAnnouncement/$', views.updateAnnouncement, name='updateAnnouncement'),
    url(r'^workBond/$', views.workBond, name='workBond'),
    # Calendars
    url(r'^management/$', views.calendarManagement, name='calendarManagement'),
    url(r'^management/rso/$', views.calendarManagementRSO, name='calendarManagementRSO'),
    url(r'^management/events/$', views.calendarManagementEVENTS, name='calendarManagementEVENTS'),
    url(r'^management/marine/$', views.calendarManagementMARINE, name='calendarManagementMARINE'),
    
    url(r'^management/announcement/$', views.calendarManagementANNOUNCEMENTS, name='calendarManagementANNOUNCEMENTS'),
    url(r'^createRSOCalendarEvent/$', views.createRSOCalendarEvent, name='createRSOCalendarEvent'),
    url(r'^updateRSOCalendar/$', views.updateRSOCalendar, name='updateRSOCalendar'),
    url(r'^updateEventCalendar/$', views.updateEventCalendar, name='updateEventCalendar'),

]