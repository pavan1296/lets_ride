import pytest
from lets_ride.constants.exception_messages import INVALID_NO_OF_SEATS
from lets_ride.constants.exception_messages import (
    INVALID_NO_OF_SEATS,
    INVALID_FLEXIBLE_DATETIME,
    INVALID_FROM_OR_TO_PLACE,
    INVALID_LUGGAGE_QUANTITY,
    INVALID_NO_OF_ASSETS,
    INVALID_WHOM_TO_DELIVER,
    INVALID_ASSET_TYPE
)


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