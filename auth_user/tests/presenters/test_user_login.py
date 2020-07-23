import pytest
import json
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from auth_user.presenters.presenter_implementation import PresenterImplementation
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS
from auth_user.tests.factories.dto_factory import UserLoginAccessTokenDTOFactoy

def test_user_login_details_returns_access_token(user_access_token_response_fixture):
    #Arrange
    presenter_input = UserLoginAccessTokenDTOFactoy()
    presenter = PresenterImplementation()
    status_code = 200
    #Act
    actual_output = presenter.user_access_token(access_token=presenter_input)
    response = json.loads(actual_output.content)
    #Assert
    assert response == user_access_token_response_fixture
    assert actual_output.status_code == status_code


def test_user_login_details_with_invalid_credentials_raises_exception(invalid_phone_number_fixture):
    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_output = presenter.raise_exception_for_invalid_phone_number()
    import json
    response = json.loads(actual_output.content)
    #Assert
    assert response == invalid_phone_number_fixture

def test_user_login_details_with_invalid_user_raises_exception(user_does_not_exist_fixture):
    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_output = presenter.raise_exception_for_user_does_not_exist()
    import json
    response = json.loads(actual_output.content)
    #Assert
    assert response == user_does_not_exist_fixture
