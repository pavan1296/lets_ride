import pytest


@pytest.fixture()
def invalid_no_of_seats_fixture():
    expected_output = {
        "response": "Please Give Positive integer field",
        "status": 400,
        "res_status": "INVALID_NO_OF_SEATS"
    }
    return expected_output

@pytest.fixture()
def invalid_luggage_quantity_fixture():
    expected_output = {
        "response": "Please Give Positive integer field",
        "status": 400,
        "res_status": "INVALID_LUGGAGE_QUANTITY"
    }
    return expected_output

@pytest.fixture()
def invalid_place_fixture():
    expected_output = {
        "response": "invalid from or to place given",
        "status": 400,
        "res_status": "INVALID_FROM_OR_TO_PLACE"
    }
    return expected_output

@pytest.fixture()
def invalid_date_time_fixture():
    expected_output = {
        "response": "invalid flexible datetime gievn",
        "status": 400,
        "res_status": "INVALID_FLEXIBLE_DATETIME"
    }
    return expected_output