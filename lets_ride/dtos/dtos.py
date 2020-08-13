from dataclasses import dataclass

@dataclass
class UserProfileDTO:
    username: str
    gender: str
    email: str
    phone_number: str
    image_url: str