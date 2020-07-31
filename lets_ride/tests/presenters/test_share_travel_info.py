import json
from lets_ride.presenters.presenter_implementation import PresenterImplementation


def test_share_travel_info_response():
    #Arrange
    presenter = PresenterImplementation()
    expected_output = 201
    #Act
    actual_output = presenter.share_travel_info_response()
    # Assert
    assert actual_output.status_code == expected_output
