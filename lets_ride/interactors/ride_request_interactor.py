from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.mixins.form_validations import RideORAssetRequestValidationMixin
from lets_ride.exceptions.exceptions import InvalidNoOfSeats, InvalidLuggageQuantity, InvalidPlaceGiven, \
    InvalidDateTimeGiven
from lets_ride.interactors.storages.dtos.dtos import RideRequestDTO


class RideRequestInteractor(RideORAssetRequestValidationMixin):

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_ride_details_from_user(self, ride_request_dto: RideRequestDTO):

        # TODO check_from_and_to_place_are_not_empty
        # TODO check_is_flexible_true_then_from_shoul_dnot_greater_than_to
        # TODO check_is_flexible_true_then_to_should_not_greater_than_current_time
        # TODO check_no_of_seats_should_not_less_than_or_equal_to_zero
        # TODO check_luggage_quantity_not_less_than_equal_to_zero
        try:
            self._check_ride_request_dto(ride_request_dto=ride_request_dto)
            return self.presenter.post_ride_request_response()
        except InvalidNoOfSeats:
            return self.presenter.raise_exception_for_invalid_no_of_seats_given()
        except InvalidLuggageQuantity:
            return self.presenter.raise_exception_for_invalid_luggage_quantity_given()
        except InvalidPlaceGiven:
            return self.presenter.raise_exception_for_invalid_place_given()
        except InvalidDateTimeGiven:
            return self.presenter.raise_exception_for_invalid_date_time_given()

    def _check_ride_request_dto(self, ride_request_dto):
        is_invalid_no_of_seats = ride_request_dto.no_of_seats <= 0
        if is_invalid_no_of_seats:
            raise InvalidNoOfSeats
        is_invalid_luggage_quantity = ride_request_dto.luggage_quantity <= 0
        if is_invalid_luggage_quantity:
            raise InvalidLuggageQuantity
        self.validate_form_request(request_dto=ride_request_dto)
        self.storage.post_ride_request_details(ride_request_dto=ride_request_dto)