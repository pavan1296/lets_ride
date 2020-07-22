from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from auth_user.storages.storage_implementation import StorageImplementation
from auth_user.presenters.presenter_implementation import PresenterImplementation
from auth_user.interactors.user_profile_interactor import UserProfileInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    user_id = [user.id]

    storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = UserProfileInteractor(
        storage=storage,
        presenter=presenter
    )

    response = interactor.get_user_profile(user_ids=user_id)
    return response