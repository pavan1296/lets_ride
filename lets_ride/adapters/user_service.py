from typing import List


class UserService:

    def get_user_details(self, user_ids: List[int]):
        from auth_user.interactors.user_profile_interactor import UserProfileInteractor
        from auth_user.presenters.presenter_implementation import PresenterImplementation
        from auth_user.storages.storage_implementation import StorageImplementation

        interactor = UserProfileInteractor(
            storage=StorageImplementation(),
            presenter=PresenterImplementation()
        )
        return interactor.get_user_dtos(user_ids=user_ids)
