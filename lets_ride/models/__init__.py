from lets_ride.models.ride_request import RideRequest
from lets_ride.models.asset_request import AssetRequest
from lets_ride.models.ride_share import RideShare
from lets_ride.models.share_travel_info import ShareTravelInfo


__all__ = [
    "RideRequest",
    "AssetRequest",
    "RideShare",
    "ShareTravelInfo"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
