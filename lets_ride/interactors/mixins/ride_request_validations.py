import datetime
from lets_ride.exceptions.exceptions import (
    InvalidNoOfSeats, InvalidLuggageQuantity, InvalidPlaceGiven, InvalidDateTimeGiven
)

class RideRequestValidationMixin:
    def validate_ride_request(self, ride_request_dto):
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