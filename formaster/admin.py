# your django admin
from django.contrib import admin
from lets_ride.models.ride_request import RideRequest


admin.site.register(RideRequest)