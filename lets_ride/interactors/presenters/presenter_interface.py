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
    def raise_exception_for_invalid_place_gievn(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_date_time_given(self):
        pass