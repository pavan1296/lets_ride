import datetime
from unittest.mock import create_autospec, patch
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.tests.factories.dto_factory import RideRequestDTOFactory


def test_ride_request_for_gievn_no_of_seats_invalid_raises_exception(invalid_no_of_seats_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_no_of_seats_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.no_of_seats = 0
    presenter.invalid_no_seats_given_returns_error_response.return_value = invalid_no_of_seats_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_no_seats_given_returns_error_response.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_invalid_luggage_quantity_given(invalid_luggage_quantity):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_luggage_quantity
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.luggage_quantity = 0
    presenter.invalid_luggage_quantity_given_returns_error_response.return_value = invalid_luggage_quantity
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_luggage_quantity_given_returns_error_response.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_invalid_from_place_given(invalid_from_or_to_place_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_from_or_to_place_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.from_place = ""
    presenter.invalid_place_given_returns_error_response.return_value = invalid_from_or_to_place_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_place_given_returns_error_response.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_invalid_to_place_given(invalid_from_or_to_place_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_from_or_to_place_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.to_place = ""
    presenter.invalid_place_given_returns_error_response.return_value = invalid_from_or_to_place_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_place_given_returns_error_response.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_invalid_flexible_time_given(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.flexible_to_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_from_date_greater_than_to_date_raises_exception(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.is_flexible = True
    ride_request_dto.flexible_from_time = datetime.datetime(2021, 12, 1, 12, 12, 12)
    ride_request_dto.flexible_to_time = datetime.datetime.now()
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_when_invalid_datetime_given_raises_exception(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.is_flexible = False
    ride_request_dto.date_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_request_with_valid_details_returns_success_response():
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.is_flexible = False
    ride_request_dto.travel_date_time = datetime.datetime(2020, 12, 12)
    # Act
    actual_output = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    print(actual_output)
    # Assert
    storage.post_ride_request_details.assert_called_once_with(ride_request_dto=ride_request_dto)
    presenter.post_ride_request_response.assert_called_once()
