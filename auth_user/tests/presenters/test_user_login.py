import pytest
import json
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from auth_user.presenters.presenter_implementation import PresenterImplementation
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


def test_user_login_details_with_invalid_credentials_raises_exception():
    #Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PHONE_NUMBER[0]
    exception_res_status = INVALID_PHONE_NUMBER[1]
    #Act
    with pytest.raises(NotFound) as err:
        actual_output = presenter.raise_exception_for_invalid_phone_number()
    #Assert
    assert err.value.message == exception_message
    assert err.value.res_status == exception_res_status


def test_user_login_details_with_invalid_user_raises_exception():
    #Arrange
    presenter = PresenterImplementation()
    exception_message = USER_DOES_NOT_EXISTS[0]
    exception_res_status = USER_DOES_NOT_EXISTS[1]
    #Act
    with pytest.raises(NotFound) as err:
        actual_output = presenter.raise_exception_for_user_does_not_exist()
    #Assert
    assert err.value.message == exception_message
    assert err.value.res_status == exception_res_status
