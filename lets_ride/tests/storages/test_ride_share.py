import pytest
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.models.ride_share import RideShare
from lets_ride.tests.factories.models import RideShareFactory


@pytest.mark.django_db
def test_post_ride_share_details():
    #Arrange
    ride_share_fctory = RideShareFactory()
    storage = StorageImplementation()
    #Act
    actual_output = storage.post_ride_share_details(ride_share_dto=ride_share_fctory)
    #Assert
    ride_id = RideShare.objects.get(id=actual_output).id
    assert actual_output == ride_id