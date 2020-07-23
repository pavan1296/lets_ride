import pytest
import datetime
from auth_user.constants.dtos import UserLoginAccessTokenDTO
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS
from auth_user.tests.factories.dto_factory import UserLoginAccessTokenDTOFactoy
from common.dtos import UserAuthTokensDTO

@pytest.fixture()
def get_access_token_dto_fixture():
    return UserAuthTokensDTO(
        user_id=1,
        access_token="DyRngpHdOSdrsiI12g12",
        refresh_token="31ty2yu2e2veut",
        expires_in=str(datetime.datetime.now())
    )

@pytest.fixture()
def user_access_token_dto_fixture():
    return UserLoginAccessTokenDTOFactoy()

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