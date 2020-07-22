import abc
from typing import List
from auth_user.constants.dtos import UserLoginAccessTokenDTO
from common.dtos import UserAuthTokensDTO
from auth_user.constants.dtos import UserProfileDTO

class PresenterInterface:

    @abc.abstractmethod
    def user_access_token(self, access_token: UserLoginAccessTokenDTO):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_phone_number(self):
        pass

    @abc.abstractmethod
    def raise_exception_for_user_does_not_exist(self):
        pass

    @abc.abstractmethod
    def user_profile_dto_response(self, user_profile_dto: List[UserProfileDTO]):
        pass

    @abc.abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass