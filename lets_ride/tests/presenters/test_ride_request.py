import pytest
import json
from lets_ride.constants.exception_messages import INVALID_NO_OF_SEATS
from lets_ride.exceptions.exceptions import InvalidNoOfSeats
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden, BadRequest
from lets_ride.presenters.presenter_implementation import PresenterImplementation
from django_swagger_utils.drf_server.exceptions import NotFound


def test_raise_exception_for_invalid_no_of_seats_given(invalid_no_of_seats_fixture):
    #Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_no_of_seats_fixture
    #Act
    actual_output = presenter.raise_exception_for_invalid_no_of_seats_given()
    response = json.loads(actual_output.content)
    #Assert
    assert response == expected_output

def test_raise_exception_for_invalid_luggage_quantity_given(invalid_luggage_quantity_fixture):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_luggage_quantity_fixture
    # Act
    actual_output = presenter.raise_exception_for_invalid_luggage_quantity_given()
    response = json.loads(actual_output.content)
    # Assert
    assert response == expected_output

def test_raise_exception_for_invalid_place_given(invalid_place_fixture):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_place_fixture
    # Act
    actual_output = presenter.raise_exception_for_invalid_place_given()
    response = json.loads(actual_output.content)
    # Assert
    assert response == expected_output

def test_raise_exception_for_invalid_date_time_given(invalid_date_time_fixture):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_date_time_fixture
    # Act
    actual_output = presenter.raise_exception_for_invalid_date_time_given()
    response = json.loads(actual_output.content)
    # Assert
    assert response == expected_output

def test_post_ride_request_response():
    presenter = PresenterImplementation()
    expected_output = 201
    #Act
    actual_output = presenter.post_ride_request_response()
    #Assert
    assert actual_output.status_code == expected_output