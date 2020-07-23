import pytest
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.models.ride_request import RideRequest
from lets_ride.tests.factories.models import RideRequestFactory


@pytest.mark.django_db
def test_post_ride_request_details():
    #Arrange
    ride_request_factory = RideRequestFactory()
    storage = StorageImplementation()
    #Act
    actual_output = storage.post_ride_request_details(ride_request_dto=ride_request_factory)
    #Assert
    ride_id = RideRequest.objects.get(id=actual_output).id
    assert ride_id == actual_output