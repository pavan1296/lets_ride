import pytest
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.interactors.storages.storage_interface import StorageInterface
from auth_user.interactors.user_profile_interactor import UserProfileInteractor
from auth_user.tests.factories.dto_factory import UserProfileFactory
from auth_user.constants.exception_messeges import USER_DOES_NOT_EXISTS
from auth_user.exceptions.exceptions import UserDoesNotExist

def test_user_profile_with_valid_data_return_response():
    #Arrange
    user_ids=[1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter
    )
    user_profile_factory = UserProfileFactory()
    storage.check_user_id_exists_in_user_model.return_value = 1
    storage.get_user_profile_dto.return_value = [user_profile_factory]
    #Act
    interactor.get_user_profile(user_ids=user_ids)
    #Assert
    presenter.user_profile_dto_response.assert_called_once_with(user_profile_dto=user_profile_factory)

def test_user_profile_with_invalid_user_raises_exception(user_does_not_exist_fixture):
    #Arrange
    # Arrange
    user_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = user_does_not_exist_fixture
    presenter.raise_exception_for_user_does_not_exist.return_value = user_does_not_exist_fixture
    #Act
    actual_output = interactor.get_user_profile(user_ids=user_ids)
    #Assert
    presenter.raise_exception_for_user_does_not_exist.assert_called_once()
    assert actual_output == expected_output