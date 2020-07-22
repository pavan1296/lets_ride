import pytest
import json
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from auth_user.constants.exception_messeges import USER_DOES_NOT_EXISTS
from auth_user.constants.dtos import UserProfileFactory
from auth_user.presenters.presenter_implementation import PresenterImplementation


def test_user_profile_with_valid_details_returns_user_profile(user_profile_fixture, user_profile_presenter_dto):
    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_output = presenter.user_profile_dto_response(user_profile_dto=user_profile_presenter_dto)
    response = json.loads(actual_output.content)
    #Assert
    assert response == user_profile_fixture

def test_user_profile_with_invalid_user_id_given():
    #Arrange
    presenter = PresenterImplementation()
    err_message = USER_DOES_NOT_EXISTS[0]
    res_status = USER_DOES_NOT_EXISTS[1]
    #Act
    with pytest.raises(NotFound) as err:
        presenter.raise_exception_for_user_does_not_exist()
    #Asserrt
    assert err.value.message == err_message
    assert err.value.res_status == res_status