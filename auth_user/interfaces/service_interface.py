from typing import List
from auth_user.constants.dtos import UserProfileDTO
from auth_user.interactors.user_profile_interactor import UserProfileInteractor


class ServiceInterface:

    @staticmethod
    def get_user_dto(user_ids: List[int]) -> UserProfileDTO:
        from auth_user.storages.storage_implementation import \
            StorageImplementation
        from auth_user.presenters.presenter_implementation import \
            PresenterImplementation
        storage = StorageImplementation()
        presenter = PresenterImplementation()

        from auth_user.interactors.user_profile_interactor import \
            UserProfileInteractor
        interactor = UserProfileInteractor(
            storage=storage, presenter=presenter
        )

        user_dtos = interactor.get_user_dtos(user_ids=user_ids)
        return user_dtos