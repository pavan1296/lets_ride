import pytest
from unittest.mock import create_autospec
from lets_ride.constants.exception_messages import (
    INVALID_NO_OF_SEATS,
    INVALID_FLEXIBLE_DATETIME,
    INVALID_FROM_OR_TO_PLACE,
    INVALID_LUGGAGE_QUANTITY,
    INVALID_NO_OF_ASSETS,
    INVALID_WHOM_TO_DELIVER,
    INVALID_ASSET_TYPE,
    INVALID_SEATS
)
from lets_ride.dtos.dtos import UserProfileDTO


@pytest.fixture()
def invalid_no_of_seats_fixture():
    expected_output = {
        "response": INVALID_NO_OF_SEATS[0],
        "status": 400,
        "res_status": INVALID_NO_OF_SEATS[1]
    }
    return expected_output


@pytest.fixture()
def invalid_flexible_datetime_fixture():
    expected_output = {
        "response": INVALID_FLEXIBLE_DATETIME[0],
        "status": 400,
        "res_status": INVALID_FLEXIBLE_DATETIME[1]
    }
    return expected_output

@pytest.fixture()
def invalid_from_or_to_place_fixture():
    expected_output = {
        "response": INVALID_FROM_OR_TO_PLACE[0],
        "status": 400,
        "res_status": INVALID_FROM_OR_TO_PLACE[1]
    }
    return expected_output

@pytest.fixture()
def invalid_luggage_quantity():
    expected_output = {
        "response": INVALID_LUGGAGE_QUANTITY[0],
        "status": 400,
        "res_status": INVALID_LUGGAGE_QUANTITY[1]
    }
    return expected_output

@pytest.fixture()
def invalid_no_of_assets_fixture():
    expected_output = {
        "response": INVALID_NO_OF_ASSETS[0],
        "status": 400,
        "res_status": INVALID_NO_OF_ASSETS[1]
    }
    return expected_output

@pytest.fixture()
def invalid_whom_to_deliver_fixture():
    expected_output = {
        "response": INVALID_WHOM_TO_DELIVER[0],
        "status": 400,
        "res_status": INVALID_WHOM_TO_DELIVER[1]
    }
    return expected_output

@pytest.fixture()
def invalid_asset_type_fixture():
    expected_output = {
        "response": INVALID_ASSET_TYPE[0],
        "status": 400,
        "res_status": INVALID_ASSET_TYPE[1]
    }
    return expected_output

@pytest.fixture()
def invalid_seats_fixture():
    expected_output = {
        "response": INVALID_SEATS[0],
        "status": 400,
        "res_status": INVALID_SEATS[1]
    }
    return expected_output

@pytest.fixture()
def storage_mock():
    from lets_ride.interactors.storages.storage_interface import StorageInterface
    storage = create_autospec(StorageInterface)
    return storage


@pytest.fixture()
def presenter_mock():
    from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
    presenter = create_autospec(PresenterInterface)
    return presenter


@pytest.fixture()
def user_profile_dto_fixture():
    user_profile_dto = [UserProfileDTO(
        username="Pavan",
        gender="MALE",
        email="pavan.medikonda@protonmail.com",
        phone_number="7799888142",
        image_url="www.imageurl.ijij0f393302r2j/32rjij3rr323r/index.html.com"
    )
    ]
    return user_profile_dto