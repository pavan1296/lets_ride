from datetime import timedelta
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.interactors.storages.dtos.dtos import RideShareDTO
from lets_ride.interactors.ride_share_interactor import RideShareInteractor
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.presenters.presenter_implementation import PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user = kwargs['user']
    request_data = dict(kwargs['request_data'])
    user_id = user.id

    if request_data['is_flexible']:
        request_data['flexible_from_time'] += timedelta(hours=5, minutes=30)
        request_data['flexible_to_time'] += timedelta(hours=5, minutes=30)
    else:
        request_data['travel_date_time'] += timedelta(hours=5, minutes=30)

    ride_share_dto = RideShareDTO(
        from_place=request_data['from_place'],
        to_place=request_data['to_place'],
        travel_date_time=request_data['travel_date_time'],
        is_flexible=request_data['is_flexible'],
        flexible_from_time=request_data['flexible_from_time'],
        flexible_to_time=request_data['flexible_to_time'],
        no_of_seats_available=request_data['no_of_seats_available'],
        assets_quantity=request_data['assets_quantity'],
        user_id=user_id
    )

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = RideShareInteractor(
        storage=storage,
        presenter=presenter
    )
    response = interactor.post_ride_share_details(ride_share_dto=ride_share_dto)
    return response