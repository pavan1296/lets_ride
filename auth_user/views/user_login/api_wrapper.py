from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from common.oauth2_storage import OAuth2SQLStorage
from auth_user.interactors.user_login_interactor import UserLoginInteractor
from auth_user.storages.storage_implementation import StorageImplementation
from auth_user.presenters.presenter_implementation import PresenterImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    credentials = kwargs['request_data']

    phone_number = dict(credentials)['phone_number']
    password = dict(credentials)['password']

    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth2_storage = OAuth2SQLStorage()
    interactor = UserLoginInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    response_data = interactor.login_validation(
        phone_number=phone_number, password=password
    )

    return response_data