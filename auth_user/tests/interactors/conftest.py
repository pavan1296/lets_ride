import pytest
import datetime
from auth_user.constants.dtos import UserLoginAccessTokenDTO
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