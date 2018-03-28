# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template
from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
# Key
# Device ID
# Time Stamp
# Status (32 bit status field)
# Temperature
# Water Level
# Battery Level
# Signal Strength




  # def __str__(self):
  #   return "%s %s" % (self.user, self.model_number, self.device_ID, self.chip_type)

# class Products(models.Model):
#   model_number = models.CharField(max_length=100)
#   laser_type = models.CharField(max_length=100)
#   power_type = models.CharField(max_length=100)
#   chip_type = models.CharField(max_length=100)


# class RegisteredDevice(models.Model):
#   device_ID = models.CharField(max_length=100,  unique=True)
#   model_number = models.ForeignKey(Products, on_delete=models.CASCADE)
#   user = models.ForeignKey(User, on_delete=models.CASCADE)
#   device_key = models.CharField(max_length=200)
#   install_date = models.DateTimeField(auto_now=True)
#   tank_depth = models.IntegerField(default=0)
#   tank_volume = models.IntegerField(default=0)
#   cross_sectional_area = models.IntegerField(default=0)

# class SensorData(models.Model):
#   device_id = models.ForeignKey(RegisteredDevice, on_delete=models.CASCADE)
#   location = models.CharField(max_length=100)
#   signal_strength = models.CharField(max_length=100)
#   transmit_time = models.CharField(max_length=100)
#   distance_cm = models.IntegerField(default=0)
#   confidence_level = models.IntegerField(default=0)
  
  # def __str__(self):
  #   return "%s %s %s %s" % (self.model_number, self.laser_type, self.power_type, self.chip_type)




# class sensor(models.Model):

#   address = models.CharField(max_length=200)
  
# # Device info would have
# # Address (location in the world)
# # Customer ID
# # Model
# # Install Date
# class sensorData(models.Model):
  
#   # device_id
#   transmission_date = models.DateTimeField(default=timezone.now)
#   # status
#   # Temperature
#   # distance


class UpdateHomePage(models.Model):
  about_section = models.TextField()
  facilities_section = models.TextField()
  general_section = models.TextField()

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

class UpdateRSOCalendar(models.Model):
  rso_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
  rso_title = models.CharField(max_length=20, default="RSO Duity")
  start_date = models.DateTimeField(blank=False)
  end_date = models.DateTimeField(blank=False)

 
