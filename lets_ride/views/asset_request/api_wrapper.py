from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTO
from lets_ride.storages.storage_implementation import StorageImplementation
from lets_ride.presenters.presenter_implementation import PresenterImplementation
from lets_ride.interactors.asset_request import AssetRequestInteractor

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = dict(kwargs['request_data'])
    user_id = user.id
    print(request_data['flexible_from_time'])
    print(request_data['flexible_to_time'])
    if request_data['is_flexible']:
        request_data['flexible_from_time'] = request_data['flexible_from_time'] + timedelta(hours=5, minutes=30)
        request_data['flexible_to_time'] = request_data['flexible_to_time'] + timedelta(hours=5, minutes=30)
    else:
        request_data['travel_date_time'] = request_data['travel_date_time'] + timedelta(hours=5, minutes=30)
    assert_requst_dto = AssetRequestDTO(
        from_place=request_data['from_place'],
        to_place=request_data['to_place'],
        travel_date_time=request_data['travel_date_time'],
        is_flexible=request_data['is_flexible'],
        flexible_from_time=request_data['flexible_from_time'],
        flexible_to_time=request_data['flexible_to_time'],
        no_of_assets=request_data['no_of_assets'],
        asset_type=request_data['asset_type'],
        asset_sensitivity=request_data['asset_sensitivity'],
        whom_to_deliver=['whom_to_deliver'],
        user_id=user_id
    )
    print(assert_requst_dto)
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = AssetRequestInteractor(
        storage=storage,
        presenter=presenter
    )
    return interactor.post_asset_request(asset_request_dto=assert_requst_dto)