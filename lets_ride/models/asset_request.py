from django.db import models
from lets_ride.constants.enums import AssetSensitivity, RideRequestStatus


class AssetRequest(models.Model):
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    travel_date_time = models.DateTimeField(auto_now=True)
    is_flexible = models.BooleanField(default=False)
    flexible_from_time = models.DateTimeField(auto_now=True)
    flexible_to_time = models.DateTimeField(auto_now=True)
    no_of_assets = models.IntegerField()
    asset_type = models.CharField(max_length=100)
    asset_sensitivity = models.CharField(AssetSensitivity.get_list_of_values(), max_length=100)
    whom_to_deliver = models.CharField(max_length=200)
    status = models.CharField(RideRequestStatus.get_list_of_values(), max_length=200, null=True)
    user_id = models.IntegerField()
