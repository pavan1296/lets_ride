from dataclasses import dataclass


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