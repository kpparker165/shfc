from django.db import models
import datetime

class Boat(models.Model):

  def __unicode__(self):
    return self.boat_name

  boat_name = models.CharField(max_length=40)
  boat_desc = models.CharField(max_length=3000)
  boat_motor = models.CharField(max_length=1000)
  boat_storage_location = models.CharField(max_length=3000)
  boat_rental_fee_full_day = models.IntegerField(default=0)
  boat_rental_fee_half_day = models.IntegerField(default=0)
  boat_creation_date = models.DateTimeField(auto_now_add=True, blank=False)


class BoatRental(models.Model):
  def __unicode__(self):
    return self.person

  boat = models.ForeignKey(Boat)
  person = models.CharField(max_length=200)
  boat_rental_start_date = models.DateTimeField(auto_now_add=True, blank=False)
  boat_rental_end_date = models.DateTimeField(auto_now_add=True, blank=False)
  boat_rental_creation_date = models.DateTimeField(auto_now_add=True, blank=False)