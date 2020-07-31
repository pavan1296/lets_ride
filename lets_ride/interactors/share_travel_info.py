from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.storages.dtos.dtos import ShareTravelInfoDTO
from lets_ride.exceptions.exceptions import InvalidAssetType, InvalidPlaceGiven, InvalidDateTimeGiven
from lets_ride.interactors.mixins.form_validations import RideORAssetRequestValidationMixin


class ShareTravelInfoInteractor(RideORAssetRequestValidationMixin):

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_share_travel_info(self, share_travel_dto: ShareTravelInfoDTO):

        # TODO: check_from_and_to_place_are_not_empty
        # TODO: check_is_flexible_true_then_from_should_not_greater_than_to
        # TODO: check_is_flexible_true_then_to_should_not_greater_than_current_time
        # TODO: check_assets_quantity_should_not_<=_0
        try:
            self._check_share_travel_info(share_travel_dto=share_travel_dto)
            return self.presenter.share_travel_info_response()
        except InvalidAssetType:
            return self.presenter.invalid_assets_given_return_error_response()
        except InvalidPlaceGiven:
            return self.presenter.invalid_place_given_returns_error_response()
        except InvalidDateTimeGiven:
            return self.presenter.invalid_date_time_given_returns_error_reponse()

    def _check_share_travel_info(self, share_travel_dto: ShareTravelInfoDTO):
        self._validate_share_travel_details(share_travel_dto=share_travel_dto)
        self.storage.post_share_travel_info(share_travel_dto=share_travel_dto)

    def _validate_share_travel_details(self, share_travel_dto: ShareTravelInfoDTO):
        is_invalid_asset_quantity = share_travel_dto.assets_quantity <= 0
        if is_invalid_asset_quantity:
            raise InvalidAssetType
        self.validate_form_request(request_dto=share_travel_dto)
