from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_invalid_no_of_seats_given(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_luggage_quantity_given(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_place_given(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date_time_given(self):
        pass

    @abstractmethod
    def post_ride_request_response(self):
        pass

    @abstractmethod
    def asset_request_response(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_asset_given(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_asset_delivery(self):
        pass

    @abstractmethod
    def return_error_response_for_invalid_asset_type_given(self):
        pass