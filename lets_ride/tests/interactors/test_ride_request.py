import pytest
from unittest.mock import create_autospec, patch
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface


def test_ride_request_for_user_retunrs_ride_details():
    #Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
