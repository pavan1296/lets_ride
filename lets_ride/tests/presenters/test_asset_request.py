import json
from lets_ride.presenters.presenter_implementation import PresenterImplementation


def test_asset_request_response():
    #Arrange
    presenter = PresenterImplementation()
    expected_output = 201
    #Act
    actual_output = presenter.asset_request_response()
    #Assert
    assert actual_output.status_code == 201

def test_raise_exception_for_invalid_asset_given(invalid_assert_given_fixture):
    #Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_assert_given_fixture
    #Act
    actual_output = presenter.raise_exception_for_invalid_asset_given()
    response = json.loads(actual_output.content)
    #Assert
    assert response == expected_output

def test_raise_exception_for_invalid_asset_delivery(invalid_asset_delivery_fixture):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_asset_delivery_fixture
    # Act
    actual_output = presenter.raise_exception_for_invalid_asset_delivery()
    response = json.loads(actual_output.content)
    #Assert
    assert response == expected_output

def test_return_error_response_for_invalid_asset_type_given(invalid_asset_type_fixture):
    # Arrange
    presenter = PresenterImplementation()
    expected_output = invalid_asset_type_fixture
    # Act
    actual_output = presenter.return_error_response_for_invalid_asset_type_given()
    response = json.loads(actual_output.content)
    #Assert
    assert response == expected_output