import datetime
from unittest import TestCase
from unittest.mock import create_autospec, patch
from lets_ride.interactors.asset_request import AssetRequestInteractor
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.tests.factories.dto_factory import AssetRequestFactory


def test_asset_request_with_invalid_no_of_assets_returns_error_message(invalid_no_of_assets_fixture):
    # Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.no_of_assets = 0
    presenter.raise_exception_for_invalid_asset_given.return_value = invalid_no_of_assets_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.raise_exception_for_invalid_asset_given.assert_called_once()
    assert actual_output == invalid_no_of_assets_fixture


def test_asset_request_when_invalid_whom_to_deliver_raise_exception(invalid_whom_to_deliver_fixture):
    # Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_whom_to_deliver_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.whom_to_deliver = ''
    presenter.raise_exception_for_invalid_asset_delivery.return_value = invalid_whom_to_deliver_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.raise_exception_for_invalid_asset_delivery.assert_called_once()
    assert actual_output == expected_output


def test_asset_request_invalid_from_place_gievn_returns_error_response(invalid_from_or_to_place_fixture):
    #Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_from_or_to_place_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.from_place = ""
    presenter.raise_exception_for_invalid_place_given.return_value = invalid_from_or_to_place_fixture
    #Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    #Assert
    presenter.raise_exception_for_invalid_place_given.assert_called_once()
    assert actual_output == expected_output

def test_asset_request_invalid_to_place_gievn_returns_error_response(invalid_from_or_to_place_fixture):
    #Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_from_or_to_place_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.to_place = ""
    presenter.raise_exception_for_invalid_place_given.return_value = invalid_from_or_to_place_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.raise_exception_for_invalid_place_given.assert_called_once()
    assert actual_output == expected_output


def test_asset_request_when_invalid_flexible_time_given(invalid_flexible_datetime_fixture):
    #Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.flexible_to_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.raise_exception_for_invalid_date_time_given.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.raise_exception_for_invalid_date_time_given.assert_called_once()
    assert actual_output == expected_output


def test_asset_request_when_given_date_time_is_invalid_return_error_response(invalid_flexible_datetime_fixture):
    # Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_flexible_datetime_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.is_flexible = False
    asset_request_dto.travel_date_time = datetime.datetime(2019, 12, 1, 12, 12, 12)
    presenter.raise_exception_for_invalid_date_time_given.return_value = invalid_flexible_datetime_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.raise_exception_for_invalid_date_time_given.assert_called_once()
    assert actual_output == expected_output


def test_asset_request_when_given_asset_type_is_integer_return_error_response(invalid_asset_type_fixture):
    # Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_asset_type_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.asset_type = 7
    presenter.return_error_response_for_invalid_asset_type_given.return_value = invalid_asset_type_fixture
    #Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    #Assert
    presenter.return_error_response_for_invalid_asset_type_given.assert_called_once()
    assert actual_output == expected_output


def test_asset_request_when_gievn_asset_type_is_null_return_error_respone(invalid_asset_type_fixture):
    # Arrange
    user_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    expected_output = invalid_asset_type_fixture
    asset_request_dto = AssetRequestFactory()
    asset_request_dto.asset_type = ""
    presenter.return_error_response_for_invalid_asset_type_given.return_value = invalid_asset_type_fixture
    # Act
    actual_output = interactor.post_asset_request(asset_request_dto=asset_request_dto, user_id=user_id)
    # Assert
    presenter.return_error_response_for_invalid_asset_type_given.assert_called_once()
    assert actual_output == expected_output