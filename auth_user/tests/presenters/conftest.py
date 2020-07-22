import pytest
from auth_user.constants.dtos import UserProfileFactory

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