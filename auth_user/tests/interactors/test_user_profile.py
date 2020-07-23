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
    storage.get_user_profile_dto.return_value = user_profile_factory
    #Act
    interactor.get_user_profile(user_ids=user_ids)
    #Assert
    presenter.user_profile_dto_response.assert_called_once_with(user_profile_dto=user_profile_factory)

def test_user_profile_with_invalid_user_raises_exception():
    #Arrange
    # Arrange
    user_ids = [1]
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter
    )
    err_message = USER_DOES_NOT_EXISTS[0]
    res_status = USER_DOES_NOT_EXISTS[1]
    storage.check_user_id_exists_in_user_model.side_effect = UserDoesNotExist
    presenter.raise_exception_for_invalid_user_id.side_effect = NotFound
    #Act
    with pytest.raises(NotFound) as err:
        interactor.get_user_profile(user_ids=user_ids)
    #Assert
    storage.check_user_id_exists_in_user_model.assert_called_once_with(user_ids=user_ids)
    presenter.raise_exception_for_invalid_user_id.assert_called_once()