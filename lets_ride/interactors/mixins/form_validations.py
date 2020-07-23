import datetime
from lets_ride.exceptions.exceptions import (
    InvalidNoOfSeats, InvalidLuggageQuantity, InvalidPlaceGiven, InvalidDateTimeGiven
)

class RideORAssetRequestValidationMixin:

    @staticmethod
    def validate_form_request(request_dto):
        is_invalid_no_of_seats = request_dto.no_of_seats <= 0
        if is_invalid_no_of_seats:
            raise InvalidNoOfSeats
        is_invalid_luggage_quantity = request_dto.luggage_quantity <= 0
        if is_invalid_luggage_quantity:
            raise InvalidLuggageQuantity
        is_valid_from_and_to_place = len(request_dto.from_place) == 0 or len(request_dto.to_place) == 0
        if is_valid_from_and_to_place:
            raise InvalidPlaceGiven
        current_date_time = datetime.datetime.now()
        if request_dto.is_flexible:
            if current_date_time > request_dto.flexible_to_time:
                raise InvalidDateTimeGiven
            elif request_dto.flexible_to_time > request_dto.flexible_from_time:
                raise InvalidDateTimeGiven
        else:
            if current_date_time > request_dto.date_time:
                raise InvalidDateTimeGiven