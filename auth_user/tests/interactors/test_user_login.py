import pytest
from unittest.mock import create_autospec, patch
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.interactors.storages.storage_interface import StorageInterface
from auth_user.interactors.user_login_interactor import UserLoginInteractor
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from django_swagger_utils.drf_server.exceptions import NotFound, Unauthorized
from auth_user.exceptions.exceptions import InvalidPhonenumber, UserDoesNotExist


def test_user_login_with_invalid_phone_number():
    #Arrange
    phone_number = "1874563210"
    password = "qwerty"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuthUserAuthTokensService)
    token_service = create_autospec(OAuthUserAuthTokensService)
    interactor = UserLoginInteractor(
        storage = storage,
        presenter = presenter,
        oauth2_storage=oauth2_storage
    )
    presenter.raise_exception_for_invalid_phone_number.side_effect = NotFound
    #Act
    with pytest.raises(NotFound):
        interactor.login_validation(phone_number=phone_number, password=password)

def test_user_login_details_with_invalid_phone_number_with_chars_raises_exception():
    #Arrange
    phone_number = "874563210i"
    password = "qwerty"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuthUserAuthTokensService)
    token_service = create_autospec(OAuthUserAuthTokensService)
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    presenter.raise_exception_for_invalid_phone_number.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.login_validation(phone_number=phone_number, password=password)


def test_user_login_details_with_phone_number_greater_than_ten_chars_raises_exception():
    phone_number = "87456321077"
    password = "qwerty"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuthUserAuthTokensService)
    token_service = create_autospec(OAuthUserAuthTokensService)
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    presenter.raise_exception_for_invalid_phone_number.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.login_validation(phone_number=phone_number, password=password)

def test_user_login_details_with_phone_number_less_than_ten_chars_raises_exception():
    phone_number = "87456321077"
    password = "qwerty"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuthUserAuthTokensService)
    token_service = create_autospec(OAuthUserAuthTokensService)
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    presenter.raise_exception_for_invalid_phone_number.side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.login_validation(phone_number=phone_number, password=password)

@patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
def test_user_login_details_return_access_token(access_token_mock, get_access_token_dto_fixture, user_access_token_dto_fixture):
    #Arrange
    user_id = 1
    phone_number = "8745632100"
    password = "qwerty"
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    oauth2_storage = create_autospec(OAuthUserAuthTokensService)
    token_service = create_autospec(OAuthUserAuthTokensService)
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )
    access_token = user_access_token_dto_fixture
    access_token_mock.return_value = get_access_token_dto_fixture
    storage.check_phone_number_and_password_exists_in_user.return_value = user_id
    #Act
    interactor.login_validation(phone_number=phone_number, password=password)
    #Assert
    presenter.user_access_token.assert_called_once_with(access_token=access_token)