import factory
from factory import Factory
import datetime
import factory.fuzzy
from auth_user.constants.dtos import UserProfileDTO, UserLoginAccessTokenDTO
from auth_user.constants.enum import GenderInformation


class UserProfileFactory(Factory):
    class Meta:
        model = UserProfileDTO
    username = "Pavan"
    gender = GenderInformation.male.value
    email = "ibcommon@ibhubs.in"
    phone_number = "7799888142"
    image_url = "www.ibhubs.co"

class UserLoginAccessTokenDTOFactoy(Factory):
    class Meta:
        model = UserLoginAccessTokenDTO

    access_token = 'DyRngpHdOSdrsiI12g12'
    user_id = 1