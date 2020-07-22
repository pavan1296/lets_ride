from typing import Optional, List
from auth_user.models import User
from auth_user.constants.dtos import UserProfileDTO
from auth_user.exceptions.exceptions import UserDoesNotExist
from auth_user.interactors.storages.storage_interface import StorageInterface


class StorageImplementation(StorageInterface):

    def check_phone_number_exists_in_user(self, phone_number: str):
        try:
            User.objects.get(phone_number=phone_number)
        except:
            raise UserDoesNotExist

    def check_phone_number_and_password_exists_in_user(self, phone_number: str, password: str):
        user = User.objects.get(phone_number=phone_number)
        if not user.check_password(password):
            raise UserDoesNotExist
        return user.id

    def check_user_id_exists_in_user_model(self, user_ids: List[int]):
        list_of_objs = User.objects.filter(id__in=user_ids)
        return len(list_of_objs)

    def get_user_profile_dto(self, user_ids: List[int]) -> List[UserProfileDTO]:
        users = User.objects.filter(id__in=user_ids)
        list_of_user_dto = []
        for user in users:
            list_of_user_dto.append(UserProfileDTO(
                username=user.username,
                gender=user.gender,
                email=user.email,
                phone_number=user.phone_number,
                image_url=user.image_url
            ))
        return list_of_user_dto