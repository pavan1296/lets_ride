import datetime
from lets_ride.exceptions.exceptions import (
    InvalidPlaceGiven, InvalidDateTimeGiven
)


class RideORAssetRequestValidationMixin:

    @staticmethod
    def validate_form_request(request_dto):
        is_valid_from_and_to_place = len(request_dto.from_place) == 0 or len(request_dto.to_place) == 0
        if is_valid_from_and_to_place:
            raise InvalidPlaceGiven
        current_date_time = datetime.datetime.now()
        if request_dto.is_flexible:
            if current_date_time > request_dto.flexible_to_time:
                raise InvalidDateTimeGiven
            elif request_dto.flexible_from_time > request_dto.flexible_to_time:
                raise InvalidDateTimeGiven
            elif current_date_time > request_dto.flexible_from_time:
                raise InvalidDateTimeGiven
        else:
            if current_date_time > request_dto.travel_date_time:
                raise InvalidDateTimeGiven
