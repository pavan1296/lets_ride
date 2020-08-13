import pytest
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.models.share_travel_info import ShareTravelInfo
from lets_ride.tests.factories.models import ShareTravelInfoFactory


@pytest.mark.django_db
def test_post_ride_share_details():
    # Arrange
    share_travel_dto = ShareTravelInfoFactory()
    storage = StorageImplementation()
    # Act
    actual_output = storage.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    share_id = ShareTravelInfo.objects.get(id=actual_output).id
    assert actual_output == share_id
