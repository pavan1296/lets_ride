from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.interactors.storages.dtos.dtos import RideRequestDTO
from lets_ride.interactors.ride_request_interactor import RideRequestInteractor
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.presenters.presenter_implementation import PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = dict(kwargs['request_data'])
    user_id = user.id

    ride_request_dto = RideRequestDTO(
        from_place=request_data['from_place'],
        to_place=request_data['to_place'],
        is_flexible=request_data['is_flexible'],
        flexible_from_time=request_data['flexible_from_time'],
        flexible_to_time=request_data['flexible_to_time'],
        no_of_seats=request_data['no_of_seats'],
        luggage_quantity=request_data['luggage_quantity'],
        travel_date_time=request_data['travel_date_time']
    )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = RideRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    response = interactor.post_ride_details_from_user(ride_request_dto=ride_request_dto)
    return response
