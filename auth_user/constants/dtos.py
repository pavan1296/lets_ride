from dataclasses import dataclass

import factory
from factory import Factory
import datetime
import string
import factory.fuzzy
from auth_user.constants.enum import GenderInformation


@dataclass
class UserLoginAccessTokenDTO:
    access_token: str
    user_id: int

@dataclass
class UserProfileDTO:
    username: str
    gender: str
    email: str
    phone_number: str
    image_url: str