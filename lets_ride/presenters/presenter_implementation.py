import json
from django.http import HttpResponse
from lets_ride.constants.exception_messages import (
    INVALID_NO_OF_SEATS,
    INVALID_FLEXIBLE_DATETIME,
    INVALID_FROM_OR_TO_PLACE,
    INVALID_LUGGAGE_QUANTITY,
    INVALID_ASSET_TYPE,
    INVALID_NO_OF_ASSETS,
    INVALID_WHOM_TO_DELIVER
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
        return HttpResponse(response, status=400)

    def raise_exception_for_invalid_luggage_quantity_given(self):
        invalid_luggage_quantity = {
            "response": INVALID_LUGGAGE_QUANTITY[0],
            "status": 400,
            "res_status": INVALID_LUGGAGE_QUANTITY[1]
        }
        response = json.dumps(invalid_luggage_quantity)
        return HttpResponse(response, status=400)

    def raise_exception_for_invalid_place_given(self):
        invalid_place = {
            "response": INVALID_FROM_OR_TO_PLACE[0],
            "status": 400,
            "res_status": INVALID_FROM_OR_TO_PLACE[1]
        }
        response = json.dumps(invalid_place)
        return HttpResponse(response, status=400)

    def raise_exception_for_invalid_date_time_given(self):
        invalid_datetime = {
            "response": INVALID_FLEXIBLE_DATETIME[0],
            "status": 400,
            "res_status": INVALID_FLEXIBLE_DATETIME[1]
        }
        response = json.dumps(invalid_datetime)
        print(response)
        return HttpResponse(response, status=400)

    def post_ride_request_response(self):
        return HttpResponse(status=201)

    def asset_request_response(self):
        return HttpResponse(status=201)

    def raise_exception_for_invalid_asset_given(self):
        invalid_assets = {
            "response": INVALID_NO_OF_ASSETS[0],
            "status": 400,
            "res_status": INVALID_NO_OF_ASSETS[1]
        }
        response = json.dumps(invalid_assets)
        return HttpResponse(response, status=400)

    def raise_exception_for_invalid_asset_delivery(self):
        invalid_delivery_address = {
            "response": INVALID_WHOM_TO_DELIVER[0],
            "status": 400,
            "res_status": INVALID_WHOM_TO_DELIVER[1]
        }
        response = json.dumps(invalid_delivery_address)
        return HttpResponse(response, status=400)

    def return_error_response_for_invalid_asset_type_given(self):
        invalid_asset_type = {
            "response": INVALID_ASSET_TYPE[0],
            "status": 400,
            "res_status": INVALID_ASSET_TYPE[1]
        }
        response = json.dumps(invalid_asset_type)
        return HttpResponse(response, status=400)