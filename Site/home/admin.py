# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import NewAnnouncement, UpdateRSOCalendar


admin.site.register(NewAnnouncement)
admin.site.register(UpdateRSOCalendar)
# admin.site.register(Products)
# admin.site.register(SensorData)
