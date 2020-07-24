from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.models.ride_request import RideRequest
from lets_ride.models.asset_request import AssetRequest
from lets_ride.tests.dtos.dtos import RideRequestDTO
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTO


class StorageImplementation(StorageInterface):

    def post_ride_request_details(self, ride_request_dto: RideRequestDTO):
        ride_request_id = RideRequest.objects.create(
            from_place=ride_request_dto.from_place,
            to_place=ride_request_dto.to_place,
            travel_date_time=ride_request_dto.travel_date_time,
            no_of_seats=ride_request_dto.no_of_seats,
            luggage_quantity=ride_request_dto.luggage_quantity,
            is_flexible=ride_request_dto.is_flexible,
            flexible_from_time=ride_request_dto.flexible_from_time,
            flexible_to_time=ride_request_dto.flexible_to_time,
            user_id=ride_request_dto.user_id
        )
        return ride_request_id.id

    def post_asset_request(self, asset_request_dto: AssetRequestDTO):
        asset_request = AssetRequest.objects.create(
            from_place=asset_request_dto.from_place,
            to_place=asset_request_dto.from_place,
            travel_date_time=asset_request_dto.travel_date_time,
            is_flexible=asset_request_dto.is_flexible,
            flexible_from_time=asset_request_dto.flexible_from_time,
            flexible_to_time=asset_request_dto.flexible_to_time,
            no_of_assets=asset_request_dto.no_of_assets,
            asset_type=asset_request_dto.asset_type,
            asset_sensitivity=asset_request_dto.asset_sensitivity,
            whom_to_deliver=asset_request_dto.whom_to_deliver,
            user_id=asset_request_dto.user_id
        )
        return asset_request.id
