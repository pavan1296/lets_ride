import datetime
from unittest.mock import create_autospec, patch
from lets_ride.interactors.share_travel_info import ShareTravelInfoInteractor
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.tests.factories.dto_factory import ShareTravelInfoFactory
from lets_ride.tests.factories.dto_factory import ShareTravelInfoFactory


def test_share_travel_info_invalid_assets_quantity_given_returns_error_response(invalid_no_of_assets_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ShareTravelInfoInteractor(
        storage=storage,
        presenter=presenter
    )
    share_travel_dto = ShareTravelInfoFactory()
    share_travel_dto.assets_quantity = 0
    expected_output = invalid_no_of_assets_fixture
    presenter.invalid_assets_given_return_error_response.return_value = invalid_no_of_assets_fixture
    # Act
    actual_output = interactor.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    presenter.invalid_assets_given_return_error_response.assert_called_once()
    assert actual_output == expected_output


def test_share_travel_info_when_invalid_flexible_time_given_returns_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ShareTravelInfoInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    share_travel_dto = ShareTravelInfoFactory()
    share_travel_dto.flexible_to_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_share_travel_info_when_from_date_greater_than_to_date_returns_error_response(
        invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ShareTravelInfoInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    share_travel_dto = ShareTravelInfoFactory()
    share_travel_dto.is_flexible = True
    share_travel_dto.flexible_from_time = datetime.datetime(2021, 12, 1, 12, 12, 12)
    share_travel_dto.flexible_to_time = datetime.datetime.now()
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_share_travel_info_when_invalid_datetime_given_returns_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ShareTravelInfoInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    share_travel_dto = ShareTravelInfoFactory()
    share_travel_dto.is_flexible = False
    share_travel_dto.date_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.invalid_date_time_given_returns_error_reponse.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    presenter.invalid_date_time_given_returns_error_reponse.assert_called_once()
    assert actual_output == expected_output


def test_share_travel_info_with_valid_details_returns_success_response():
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = ShareTravelInfoInteractor(
        storage=storage,
        presenter=presenter
    )
    share_travel_dto = ShareTravelInfoFactory()
    share_travel_dto.is_flexible = False
    share_travel_dto.travel_date_time = datetime.datetime(2020, 12, 12)
    # Act
    actual_output = interactor.post_share_travel_info(share_travel_dto=share_travel_dto)
    # Assert
    storage.post_share_travel_info.assert_called_once_with(share_travel_dto=share_travel_dto)
    presenter.share_travel_info_response.assert_called_once()