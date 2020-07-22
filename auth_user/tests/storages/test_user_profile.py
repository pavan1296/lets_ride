import pytest
from auth_user.storages.storage_implementation import StorageImplementation
from django_swagger_utils.drf_server.exceptions import NotFound, Unauthorized
from auth_user.factory import UserFactory
from auth_user.exceptions.exceptions import UserDoesNotExist
from auth_user.constants.exception_messeges import USER_DOES_NOT_EXISTS


@pytest.mark.django_db
def test_user_profile_with_invalid_user_id_raises_exception():
    #Arrange
    user_ids = [7]
    length = 0
    storage = StorageImplementation()
    #Act
    actual_output = storage.check_user_id_exists_in_user_model(user_ids=user_ids)
    assert actual_output == length

@pytest.mark.django_db
def test_user_profile_with_valid_details_returns_user_dto(user):
    #Arrange
    storage = StorageImplementation()
    user_ids = [1]
    #Act
    actual_output = storage.get_user_profile_dto(user_ids=user_ids)
    #Assert
    assert actual_output[0].username == user.username
    assert actual_output[0].phone_number == user.phone_number
    assert actual_output[0].email == user.email
    assert actual_output[0].gender == user.gender
