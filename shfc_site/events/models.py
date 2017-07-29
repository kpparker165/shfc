from django.db import models
import datetime

TYPE = (
  ('success', 'Event'),
  ('warning', 'Notification'),
  ('danger', 'Closure'),
)
class Event(models.Model):

  def __unicode__(self):
    return self.event_name

  event_name = models.CharField(max_length=200)
  event_desc = models.CharField(max_length = 1000)
  event_creation_date = models.DateTimeField(auto_now_add=True, blank=False)
  event_start_date = models.DateTimeField(blank=False)
  event_end_date = models.DateTimeField(blank=False)
  event_type= models.CharField(max_length=7, choices=TYPE, default='success')