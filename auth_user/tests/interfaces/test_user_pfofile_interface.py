import pytest
from unittest.mock import create_autospec, patch
from auth_user.interfaces.service_interface import ServiceInterface
from auth_user.tests.factories.dto_factory import UserProfileFactory
from auth_user.interactors.user_profile_interactor import UserProfileInteractor

@patch.object(UserProfileInteractor, 'get_user_dtos')
def test_user_id_returns_user_dtos(user_profile_dto_mock):
    #Arrange
    user_ids = [1]
    user_profile = UserProfileFactory()
    user_profile_dto_mock.return_value = user_profile
    #Act
    actual_output = ServiceInterface.get_user_dto(user_ids=user_ids)
    #Assert
    assert actual_output == user_profile