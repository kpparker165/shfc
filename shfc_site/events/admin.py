from events.models import Event
from django.contrib import admin

class EventsAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,               {'fields': ['event_type','event_name','event_desc']}),
    ('Date information', {'fields': ['event_start_date','event_end_date']}),
  ]
  list_display = ( 'event_name', 'event_desc', 'event_creation_date')
  list_filter = ['event_creation_date',]
  search_fields = ['event_name']
  date_hierarchy = 'event_creation_date'
  readonly_fields = ("event_creation_date",)
admin.site.register(Event, EventsAdmin)


