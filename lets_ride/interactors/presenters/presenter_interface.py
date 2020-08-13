from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def invalid_no_seats_given_returns_error_response(self):
        pass

    @abstractmethod
    def invalid_luggage_quantity_given_returns_error_response(self):
        pass

    @abstractmethod
    def invalid_place_given_returns_error_response(self):
        pass

    @abstractmethod
    def invalid_date_time_given_returns_error_reponse(self):
        pass

    @abstractmethod
    def post_ride_request_response(self):
        pass

    @abstractmethod
    def asset_request_response(self):
        pass

    @abstractmethod
    def invalid_assets_given_return_error_response(self):
        pass

    @abstractmethod
    def invalid_assets_delivery_given_returns_error_response(self):
        pass

    @abstractmethod
    def return_error_response_for_invalid_asset_type_given(self):
        pass

    @abstractmethod
    def invalid_no_of_seats_returns_error_message(self):
        pass

    @abstractmethod
    def share_ride_response(self):
        pass


    @abstractmethod
    def invalid_assets_quantity_given_returns_error_message(self):
        pass

    @abstractmethod
    def share_travel_info_response(self):
        pass

    @abstractmethod
    def invalid_user_given_returns_error_response(self):
        pass

    @abstractmethod
    def share_ride_details_response_details(self, share_ride_details):
        pass