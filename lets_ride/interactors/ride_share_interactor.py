from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.mixins.form_validations import RideORAssetRequestValidationMixin
from lets_ride.exceptions.exceptions import InvalidPlaceGiven, \
    InvalidDateTimeGiven, InvalidAssetType, InvalidNoOfSeats
from lets_ride.interactors.storages.dtos.dtos import RideShareDTO


class RideShareInteractor(RideORAssetRequestValidationMixin):

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_ride_share_details(self, ride_share_dto: RideShareDTO):

        # TODO: check_from_and_to_place_are_not_empty
        # TODO: check_is_flexible_true_then_from_should_not_greater_than_to
        # TODO: check_is_flexible_true_then_to_should_not_greater_than_current_time
        # TODO: check_no_of_seats_less_than_or_equal_to_zero
        # TODO: check_asset_quantity_less_than_or_equal_to_zero
        try:
            self.check_ride_share_details(ride_share_dto=ride_share_dto)
            return self.presenter.share_ride_response()
        except InvalidNoOfSeats:
            return self.presenter.invalid_no_of_seats_returns_error_message()
        except InvalidAssetType:
            return self.presenter.invalid_assets_quantity_given_returns_error_message()
        except InvalidPlaceGiven:
            return self.presenter.invalid_place_given_returns_error_response()
        except InvalidDateTimeGiven:
            return self.presenter.invalid_date_time_given_returns_error_reponse()

    def check_ride_share_details(self, ride_share_dto: RideShareDTO):
        self._validate_ride_share_dto(ride_share_dto=ride_share_dto)
        self.storage.post_ride_share_details(ride_share_dto=ride_share_dto)

    def _validate_ride_share_dto(self, ride_share_dto: RideShareDTO):
        is_invalid_seats_quantity = ride_share_dto.no_of_seats_available <= 0
        if is_invalid_seats_quantity:
            raise InvalidNoOfSeats

        is_invalid_assets_quantity = ride_share_dto.assets_quantity <= 0

        if is_invalid_assets_quantity:
            raise InvalidAssetType

        self.validate_form_request(request_dto=ride_share_dto)
