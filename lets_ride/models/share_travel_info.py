from django.db import models
from lets_ride.constants.enums import TravelMedium, ShareTravelStatus


class ShareTravelInfo(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(auto_now=True)
    is_flexible = models.BooleanField(default=False)
    flexible_from_time = models.DateTimeField(auto_now=True)
    flexible_to_time = models.DateTimeField(auto_now=True)
    travel_medium = models.CharField(TravelMedium.get_list_of_names(),max_length=100, null=True)
    status = models.CharField(ShareTravelStatus.get_list_of_values(), max_length=20, null=True)
    user_id = models.IntegerField(null=True)
    ride_requests = models.IntegerField(null=True)
    assets_quantity = models.IntegerField()
