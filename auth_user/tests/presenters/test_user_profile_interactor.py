import pytest
import json
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from auth_user.constants.exception_messeges import USER_DOES_NOT_EXISTS
from auth_user.tests.factories.dto_factory import UserProfileFactory
from auth_user.presenters.presenter_implementation import PresenterImplementation


def test_user_profile_with_valid_details_returns_user_profile(user_profile_fixture, user_profile_presenter_dto):
    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_output = presenter.user_profile_dto_response(user_profile_dto=user_profile_presenter_dto)
    response = json.loads(actual_output.content)
    #Assert
    assert response == user_profile_fixture

def test_user_profile_with_invalid_user_id_given(user_does_not_exist_fixture):
    #Arrange
    presenter = PresenterImplementation()
    #Act
    actual_output = presenter.raise_exception_for_user_does_not_exist()
    response = json.loads(actual_output.content)
    #Asserrt
    assert response == user_does_not_exist_fixture