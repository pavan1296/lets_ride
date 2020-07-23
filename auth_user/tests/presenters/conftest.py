import pytest
from auth_user.tests.factories.dto_factory import UserProfileFactory
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS

@pytest.fixture()
def user_access_token_response_fixture():
    access_token_dict = {
        "access_token": "DyRngpHdOSdrsiI12g12",
        "user_id": 1
    }
    return access_token_dict

@pytest.fixture()
def user_profile_fixture():
    expected_user_profile = [{
        "name": "Pavan",
        "gender": "MALE",
        "email": "ibcommon@ibhubs.in",
        "phone_number": "7799888142",
        "image_url": "www.ibhubs.co"
    }]
    return expected_user_profile

@pytest.fixture()
def user_profile_presenter_dto():
    return [UserProfileFactory()]

@pytest.fixture()
def invalid_phone_number_fixture():
    expected_output = {
        "response": INVALID_PHONE_NUMBER[0],
        "status": 400,
        "res_status": INVALID_PHONE_NUMBER[1]
    }
    return expected_output

@pytest.fixture()
def user_does_not_exist_fixture():
    expected_output = {
        "response": USER_DOES_NOT_EXISTS[0],
        "status": 400,
        "res_status": USER_DOES_NOT_EXISTS[1]
    }
    return expected_output