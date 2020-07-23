from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.models.ride_request import RideRequest
from lets_ride.tests.dtos.dtos import RideRequestDTO


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
            flexible_to_time=ride_request_dto.flexible_to_time
        )
        return ride_request_id.id
