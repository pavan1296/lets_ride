import json
from lets_ride.presenters.presenter_implementation import PresenterImplementation

def test_invalid_no_of_seats_returns_error_message(invalid_seats_fixture):
    #Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_seats_fixture
    #Act
    actual_output = presenter.invalid_no_of_seats_returns_error_message()
    response = json.loads(actual_output.content)
    #Assert
    assert response == expected_output


def test_invalid_asset_quantity_given_returns_error_message(invalid_asset_type_fixture):
    #Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_asset_type_fixture
    #Act
    actual_output = presenter.invalid_assets_quantity_given_returns_error_message()
    response = json.loads(actual_output.content)
    # Assert
    assert response == expected_output


def test_share_ride_response():
    #Arrange
    presenter = PresenterImplementation()
    expected_output = 201
    #Act
    actual_output = presenter.share_ride_response()
    # Assert
    assert actual_output.status_code == expected_output