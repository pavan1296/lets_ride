from typing import List
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.interactors.storages.storage_interface import StorageInterface
from auth_user.exceptions.exceptions import UserDoesNotExist


class UserProfileInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_user_profile(self, user_ids: List[int]):

        #TODO: check user_ids exists in user model
        try:
            user_profile_dto = self._check_user_id_exists_in_user(user_ids=user_ids)
            return self.presenter.user_profile_dto_response(user_profile_dto=user_profile_dto)
        except UserDoesNotExist:
            return self.presenter.raise_exception_for_user_does_not_exist()

    def _check_user_id_exists_in_user(self, user_ids: List[int]):
        self._check_list_of_user_ids_present_in_user(user_ids=user_ids)
        list_of_user_dtos = self.storage.get_user_profile_dto(user_ids=user_ids)
        return list_of_user_dtos

    def _check_list_of_user_ids_present_in_user(self, user_ids: List[int]):
        len_of_objs = self.storage.check_user_id_exists_in_user_model(user_ids=user_ids)
        is_invalid_ids = len_of_objs != len(user_ids)
        if is_invalid_ids:
            raise UserDoesNotExist

    def get_user_dtos(self, user_ids: List[int]):
        self._check_list_of_user_ids_present_in_user(user_ids=user_ids)
        list_of_user_dtos = self.storage.get_user_profile_dto(user_ids=user_ids)
        return list_of_user_dtos
