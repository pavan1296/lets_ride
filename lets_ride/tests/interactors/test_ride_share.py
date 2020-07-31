import datetime
from unittest.mock import create_autospec, patch
from lets_ride.interactors.ride_share_interactor import RideShareInteractor
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.tests.factories.dto_factory import RideShareDTOFactory


def test_ride_share_details_with_invalid_no_of_seats_available_returns_error_response(invalid_seats_fixture):
    #Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_seats_fixture
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.no_of_seats_available = 0
    presenter.invalid_no_of_seats_returns_error_message.return_value = invalid_seats_fixture
    #Act
    actual_output = interactor.post_ride_share_details(
        ride_share_dto=ride_share_dto
    )
    #Assert
    presenter.invalid_no_of_seats_returns_error_message.assert_called_once()
    assert actual_output == expected_output


def test_ride_share_details_with_invalid_assets_quantity_returns_error_response(invalid_asset_type_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_asset_type_fixture
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.assets_quantity = 0
    presenter.invalid_assets_quantity_given_returns_error_message.return_value = invalid_asset_type_fixture
    #Act
    actual_output = interactor.post_ride_share_details(
        ride_share_dto=ride_share_dto
    )
    #Assert
    presenter.invalid_assets_quantity_given_returns_error_message.assert_called_once()
    assert actual_output == expected_output


def test_ride_share_when_invalid_flexible_time_given_returns_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.flexible_to_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_share_details(ride_share_dto=ride_share_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_share_when_from_date_greater_than_to_date_returns_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.is_flexible = True
    ride_share_dto.flexible_from_time = datetime.datetime(2021, 12, 1, 12, 12, 12)
    ride_share_dto.flexible_to_time = datetime.datetime.now()
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_share_details(ride_share_dto=ride_share_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_share_when_invalid_datetime_given_returns_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.is_flexible = False
    ride_share_dto.date_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_ride_share_details(ride_share_dto=ride_share_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_ride_share_with_valid_details_returns_success_response():
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_share_dto = RideShareDTOFactory()
    ride_share_dto.is_flexible = False
    ride_share_dto.travel_date_time = datetime.datetime(2020, 12, 12)
    # Act
    actual_output = interactor.post_ride_share_details(ride_share_dto=ride_share_dto)
    # Assert
    storage.post_ride_share_details.assert_called_once_with(ride_share_dto=ride_share_dto)
    presenter.share_ride_response.assert_called_once()