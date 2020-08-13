from lets_ride.adapters.service_adapter import get_service_adapter
from unittest.mock import patch
from auth_user.interactors.user_profile_interactor import UserProfileInteractor


@patch.object(UserProfileInteractor, 'get_user_dtos')
def test_get_service_adapter_with_valid_ids_returns_error_response(profile_mock, user_profile_dto_fixture):
    # Arrange
    user_ids = [1, 2]
    service_adapter = get_service_adapter()
    profile_mock.return_value = user_profile_dto_fixture
    # Act
    user_dto = service_adapter.user_service.get_user_details(user_ids=user_ids)
    # Assert
    assert user_dto == user_profile_dto_fixture
