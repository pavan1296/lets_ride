import pytest
from lets_ride.dtos.dtos import UserProfileDTO


@pytest.fixture()
def user_profile_dto_fixture():
    user_profile_dto = [UserProfileDTO(
        username="Pavan",
        gender="MALE",
        email="pavan.medikonda@protonmail.com",
        phone_number="7799888142",
        image_url="www.imageurl.ijij0f393302r2j/32rjij3rr323r/index.html.com"
    ),
        UserProfileDTO(
            username="Pavan",
            gender="MALE",
            email="pavan.medikonda@protonmail.com",
            phone_number="7093414223",
            image_url="www.imageurl.ijij0f393302r2j/32rjij3rr323r/index.html.com"
        )
    ]
    return user_profile_dto