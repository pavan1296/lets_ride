from django.db import models
from lets_ride.constants.enums import RideRequestStatus


class RideRequest(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(auto_now=True)
    no_of_seats = models.IntegerField()
    luggage_quantity = models.IntegerField()
    is_flexible = models.BooleanField(default=False)
    flexible_from_time = models.DateTimeField(auto_now=True)
    flexible_to_time = models.DateTimeField(auto_now=True)
    status = models.CharField(RideRequestStatus.get_list_of_values(), max_length=20, null=True)
    user_id = models.IntegerField(null=True)
