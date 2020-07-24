import pytest
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTOFactory
from lets_ride.models import AssetRequest



@pytest.mark.django_db
def test_post_asset_request():
    #Arrange
    storage = StorageImplementation()
    asset_request_dto = AssetRequestDTOFactory
    print(asset_request_dto)
    #Act
    actual_output = storage.post_asset_request(asset_request_dto=asset_request_dto)
    #Assert
    is_valid = AssetRequest.objects.filter(id=actual_output).exists()
    assert True == is_valid