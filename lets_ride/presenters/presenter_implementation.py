import json
from django.http import HttpResponse
from lets_ride.constants.exception_messages import (
    INVALID_NO_OF_SEATS,
    INVALID_FLEXIBLE_DATETIME,
    INVALID_FROM_OR_TO_PLACE,
    INVALID_LUGGAGE_QUANTITY,
)
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_no_of_seats_given(self):
        invalid_no_of_seats = {
            "response": INVALID_NO_OF_SEATS[0],
            "status": 400,
            "res_status": INVALID_NO_OF_SEATS[1]
        }
        response = json.dumps(invalid_no_of_seats)
        return HttpResponse(response)

    def raise_exception_for_invalid_luggage_quantity_given(self):
        invalid_luggage_quantity = {
            "response": INVALID_LUGGAGE_QUANTITY[0],
            "status": 400,
            "res_status": INVALID_LUGGAGE_QUANTITY[1]
        }
        response = json.dumps(invalid_luggage_quantity)
        return HttpResponse(response)

    def raise_exception_for_invalid_place_gievn(self):
        invalid_place = {
            "response": INVALID_FROM_OR_TO_PLACE[0],
            "status": 400,
            "res_status": INVALID_FROM_OR_TO_PLACE[1]
        }
        response = json.dumps(invalid_place)
        return HttpResponse(response)

    def raise_exception_for_invalid_date_time_given(self):
        invalid_datetime = {
            "response": INVALID_FLEXIBLE_DATETIME[0],
            "status": 400,
            "res_status": INVALID_FLEXIBLE_DATETIME[1]
        }
        response = json.dumps(invalid_datetime)
        return HttpResponse(response)

    def post_ride_request_response(self):
        return HttpResponse(status=201)