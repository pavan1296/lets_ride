from abc import abstractmethod
from lets_ride.tests.dtos.dtos import RideRequestDTO
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTO

class StorageInterface:

    @abstractmethod
    def post_ride_request_details(self, ride_request_dto: RideRequestDTO):
        pass

    @abstractmethod
    def post_asset_request(self, asset_request_dto: AssetRequestDTO):
        pass

