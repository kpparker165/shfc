# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.db import models
from django.contrib.auth.models import User, Group


class NewAnnouncement(models.Model):
  ANNOUNCEMENT_TYPES = (
        ('danger', 'Critical'),
        ('info', 'Information'),
        ('warning', 'Warning'),
    )
  announcement_title = models.CharField(max_length=60, blank=False)
  announcement_type = models.CharField(max_length=7, choices=ANNOUNCEMENT_TYPES, blank=False)
  announcement_description = models.TextField(blank=False)
  announcement_date = models.DateTimeField(auto_now=True, blank=False)
  announcement_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  class Meta:
        permissions=(
             ("edit_announcements","Can edit announcements"),
        )

class UpdateRSOCalendar(models.Model):
  rso_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  start_date = models.DateTimeField(blank=False)
  end_date = models.DateTimeField(blank=False)
  class Meta:
        permissions=(
             ("edit_rso_calendar","Can edit rso calendar"),
             ("edit_rso_calendar_admin","Can edit calendar_admin"),
        )


class UpdateEventsCalendar(models.Model):
  events_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  start_date = models.DateTimeField(blank=False)
  end_date = models.DateTimeField(blank=False)
  events_description = models.TextField(blank=False)
  class Meta:
        permissions=(
             ("edit_events_calendar","Can edit events calendar"),
             ("edit_events_calendar_admin","Can edit calendar_admin"),
        )

 
