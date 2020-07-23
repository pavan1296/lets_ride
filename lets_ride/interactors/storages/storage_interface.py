from abc import abstractmethod
from lets_ride.tests.dtos.dtos import RideRequestDTO


class StorageInterface:

    @abstractmethod
    def post_ride_request_details(self, ride_request_dto) -> RideRequestDTO:
        pass

