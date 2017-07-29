from boats.models import Boat, BoatRental
from django.contrib import admin


# class BoatReservationAdmin(admin.ModelAdmin):
#   fieldsets = [
#     ("Reservation Information",               {'fields': ['boat','person','boat_rental_creation_date' ]}),
#     ("Rental Fees", {'fields': ['boat_rental_fee_half_day','boat_rental_fee_full_day']})
#   ]

class BoatsAdmin(admin.ModelAdmin):
  fieldsets = [
    ("Boat Information",               {'fields': ['boat_name','boat_motor','boat_desc',
    	'boat_storage_location', ]}),
    ("Rental Fees", {'fields': ['boat_rental_fee_half_day','boat_rental_fee_full_day']})
  ]
  list_display = ( 'boat_name', 'boat_desc','boat_rental_fee_half_day',
  	'boat_rental_fee_full_day')
  list_filter = ['boat_name',]
  search_fields = ['boat_name']
  date_hierarchy = 'boat_creation_date'
  readonly_fields = ("boat_creation_date",)

admin.site.register(Boat, BoatsAdmin)
admin.site.register(BoatRental)

# boat_name = models.CharField(max_length=40)
#   boat_desc = models.CharField(max_length=3000)
#   boat_motor = models.CharField(max_length=1000)
#   boat_storage_location = models.CharField(max_length=3000)
#   boat_rental_fee = models.IntegerField(blank=True)
