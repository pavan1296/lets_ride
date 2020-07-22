import pytest
from auth_user.storages.storage_implementation import StorageImplementation
from django_swagger_utils.drf_server.exceptions import NotFound, Unauthorized
from auth_user.exceptions.exceptions import UserDoesNotExist
from auth_user.constants.exception_messeges import USER_DOES_NOT_EXISTS

@pytest.mark.django_db
def test_phone_number_is_invalid_raises_exception():
    # Arrange
    storage = StorageImplementation()
    phone_number = "7799888142"
    #Act
    with pytest.raises(UserDoesNotExist) as err:
        storage.check_phone_number_exists_in_user(phone_number=phone_number)

@pytest.mark.django_db
def test_user_login_details_return_user_id(user):
    #Arrange
    storage = StorageImplementation()
    expected_output = 1
    phone_number = user.phone_number
    password = 'pavan'
    #Act
    actual_ouptput = storage.check_phone_number_and_password_exists_in_user(phone_number=phone_number, password=password)
    #Assert
    assert actual_ouptput == expected_output