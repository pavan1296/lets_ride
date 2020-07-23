import datetime
from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface
from lets_ride.interactors.mixins.ride_request_validations import RideRequestValidationMixin
from lets_ride.exceptions.exceptions import InvalidNoOfSeats, InvalidLuggageQuantity, InvalidPlaceGiven, InvalidDateTimeGiven


class RideRequestInteractor(RideRequestValidationMixin):

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def post_ride_details_from_user(self, ride_request_dto: str):

        #TODO check_from_and_to_place_are_not_empty
        #TODO check_is_flexible_true_then_from_shouldnot_greater_than_to
        #TODO check_is_flexible_true_then_to_shouldnot_greater_than_current_time
        #TODO check_no_of_seats_should_not_less_than_or_equal_to_zero
        #TODO check_luggage_qunatity_not_less_than_equal_to_zero
       try:
           self._check_ride_request_dto(ride_request_dto=ride_request_dto)
       except InvalidNoOfSeats:
           self.presenter.raise_exception_for_invalid_no_of_seats_given()
       except InvalidLuggageQuantity:
           self.presenter.raise_exception_for_invalid_luggage_quantity_given()
       except InvalidPlaceGiven:
           self.presenter.raise_exception_for_invalid_place_gievn()
       except InvalidDateTimeGiven:
           self.presenter.raise_exception_for_invalid_date_time_given()

    def _check_ride_request_dto(self, ride_request_dto):
        self.validate_ride_request(ride_request_dto=ride_request_dto)
        # self.check_given_data_is_valid(ride_request_dto=ride_request_dto)


    @staticmethod
    def check_given_data_is_valid(ride_request_dto):
        is_invalid_no_of_seats = ride_request_dto.no_of_seats <= 0
        if is_invalid_no_of_seats:
            raise InvalidNoOfSeats
        is_invalid_luggage_quantity = ride_request_dto.luggage_quantity <= 0
        if is_invalid_luggage_quantity:
            raise InvalidLuggageQuantity
        is_valid_from_and_to_place = len(ride_request_dto.from_place) == 0 or len(ride_request_dto.to_place) == 0
        if is_valid_from_and_to_place:
            raise InvalidPlaceGiven
        current_date_time = datetime.datetime.now()
        if ride_request_dto.is_flexible:
            if current_date_time > ride_request_dto.flexible_to_time:
                raise InvalidDateTimeGiven
            elif ride_request_dto.flexible_to_time > ride_request_dto.flexible_from_time:
                raise InvalidDateTimeGiven
        else:
            if current_date_time > ride_request_dto.date_time:
                raise InvalidDateTimeGiven