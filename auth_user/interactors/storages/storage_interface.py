import abc
from typing import List
from auth_user.constants.dtos import UserProfileDTO

class StorageInterface:

    @abc.abstractmethod
    def check_phone_number_and_password_exists_in_user(self, phone_number: str, password: str):
        pass

    @abc.abstractmethod
    def check_phone_number_exists_in_user(self, phone_number: str):
        pass

    @abc.abstractmethod
    def check_user_id_exists_in_user_model(self, user_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_user_profile_dto(self, user_ids: List[int]) -> UserProfileDTO:
        pass