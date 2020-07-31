from abc import abstractmethod
from lets_ride.tests.dtos.dtos import RideRequestDTO, RideShareDTO
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTO, ShareTravelInfoDTO

class StorageInterface:

    @abstractmethod
    def post_ride_request_details(self, ride_request_dto: RideRequestDTO):
        pass

    @abstractmethod
    def post_asset_request(self, asset_request_dto: AssetRequestDTO):
        pass

    @abstractmethod
    def post_ride_share_details(self, ride_share_dto: RideShareDTO):
        pass

    @abstractmethod
    def post_share_travel_info(self, share_travel_dto: ShareTravelInfoDTO):
        pass