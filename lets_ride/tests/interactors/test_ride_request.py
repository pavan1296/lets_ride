import pytest
import datetime
from unittest.mock import create_autospec, patch
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.exceptions.exceptions import InvalidNoOfSeats, InvalidLuggageQuantity, InvalidPlaceGiven, InvalidDateTimeGiven
from lets_ride.tests.dtos.dtos import RideRequestDTOFactory


def test_ride_request_for_gievn_no_of_seats_invalid_raises_exception():
    #Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.no_of_seats = 0
    presenter.raise_exception_for_invalid_no_of_seats_given.side_effect = InvalidNoOfSeats
    #Act
    with pytest.raises(InvalidNoOfSeats):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    #Assert
    presenter.raise_exception_for_invalid_no_of_seats_given.assert_called_once()

def test_ride_request_when_invalid_luggage_quantity_given():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.luggage_quantity = 0
    presenter.raise_exception_for_invalid_luggage_quantity_given.side_effect = InvalidLuggageQuantity
    #Act
    with pytest.raises(InvalidLuggageQuantity):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    #Assert
    presenter.raise_exception_for_invalid_luggage_quantity_given.assert_called_once()

def test_ride_request_when_invalid_from_place_given():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.from_place = ""
    presenter.raise_exception_for_invalid_place_gievn.side_effect = InvalidPlaceGiven
    #Act
    with pytest.raises(InvalidPlaceGiven):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    #Assert
    presenter.raise_exception_for_invalid_place_gievn.assert_called_once()

def test_ride_request_when_invalid_to_place_given():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.to_place = ""
    presenter.raise_exception_for_invalid_place_gievn.side_effect = InvalidPlaceGiven
    # Act
    with pytest.raises(InvalidPlaceGiven):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.raise_exception_for_invalid_place_gievn.assert_called_once()

def test_ride_request_when_invalid_flexible_time_given():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.flexible_to_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.raise_exception_for_invalid_date_time_given.side_effect = InvalidDateTimeGiven
    # Act
    with pytest.raises(InvalidDateTimeGiven):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    #Assert
    presenter.raise_exception_for_invalid_date_time_given.assert_called_once()


def test_ride_request_when_from_date_greater_than_to_date_raises_exception():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.is_flexible = True
    ride_request_dto.flexible_from_time = datetime.datetime(2021, 12, 1, 12, 12, 12)
    ride_request_dto.flexible_to_time = datetime.datetime.now()
    presenter.raise_exception_for_invalid_date_time_given.side_effect = InvalidDateTimeGiven
    # Act
    with pytest.raises(InvalidDateTimeGiven):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.raise_exception_for_invalid_date_time_given.assert_called_once()


def test_ride_request_when_invalid_datetime_given_raises_exception():
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    ride_request_dto = RideRequestDTOFactory()
    ride_request_dto.is_flexible = False
    ride_request_dto.date_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.raise_exception_for_invalid_date_time_given.side_effect = InvalidDateTimeGiven
    # Act
    with pytest.raises(InvalidDateTimeGiven):
        interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    # Assert
    presenter.raise_exception_for_invalid_date_time_given.assert_called_once()
