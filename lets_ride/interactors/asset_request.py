from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.mixins.form_validations import RideORAssetRequestValidationMixin
from lets_ride.exceptions.exceptions import InvalidNoOfAssets, InvalidPlaceGiven, \
    InvalidDateTimeGiven, InvalidDeliveryAddress, InvalidAssetType
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTO


class AssetRequestInteractor(RideORAssetRequestValidationMixin):

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_asset_request(self, asset_request_dto: AssetRequestDTO):
        # TODO: check_no_of_assets_less_than_or_equal_to_zero
        # TODO: check_whom_to_deliver_should_not_be_empty
        # TODO: check_from_and_to_place_are_not_empty
        # TODO: check_is_flexible_true_then_from_should_not_greater_than_to
        # TODO: check_is_flexible_true_then_to_should_not_greater_than_current_time
        try:
            self._check_asset_request(asset_request_dto=asset_request_dto)
            return self.presenter.asset_request_response()
        except InvalidNoOfAssets:
            return  self.presenter.raise_exception_for_invalid_asset_given()
        except InvalidDeliveryAddress:
            return self.presenter.raise_exception_for_invalid_asset_delivery()
        except InvalidPlaceGiven:
            return self.presenter.raise_exception_for_invalid_place_given()
        except InvalidDateTimeGiven:
            return self.presenter.raise_exception_for_invalid_date_time_given()
        except InvalidAssetType:
            return self.presenter.return_error_response_for_invalid_asset_type_given()

    def _check_asset_request(self, asset_request_dto: AssetRequestDTO):
        print("$"*100)
        self._check_validations_for_asset_dto(asset_request_dto=asset_request_dto)
        print("^"*100)
        self.storage.post_asset_request(asset_request_dto=asset_request_dto)

    def _check_validations_for_asset_dto(self, asset_request_dto: AssetRequestDTO):
        is_invalid_asset_quantity = asset_request_dto.no_of_assets <= 0
        if is_invalid_asset_quantity:
            raise InvalidNoOfAssets
        is_invalid_whom_to_deliver = len(asset_request_dto.whom_to_deliver) == 0
        if is_invalid_whom_to_deliver:
            raise InvalidDeliveryAddress
        is_invalid_asset_type = type(asset_request_dto.asset_type) == int
        if is_invalid_asset_type:
            raise InvalidAssetType
        is_invalid_asset_type = len(asset_request_dto.asset_type) == 0
        if is_invalid_asset_type:
            raise InvalidAssetType
        self.validate_form_request(request_dto=asset_request_dto)