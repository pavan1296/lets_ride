import pytest
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from unittest.mock import create_autospec, patch
from lets_ride.adapters.service_adapter import get_service_adapter
from auth_user.interactors.user_profile_interactor import UserProfileInteractor
from lets_ride.interactors.get_share_ride_details import GetShareRideDetailsInteractor


@patch.object(UserProfileInteractor, 'get_user_dtos')
def test_get_share_ride_details_user_id_given_returns_error_respone(user_dto_mock, user_profile_dto_fixture):
    # Arrange
    user_id = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetShareRideDetailsInteractor(
        storage=storage,
        presenter=presenter
    )
    user_dto_mock.return_value = user_profile_dto_fixture[0]
    #Act
    response = interactor.get_share_ride_details(user_ids=user_id)
    #Assert
    presenter.share_ride_details_response_details.assert_called_once()