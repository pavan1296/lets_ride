import json
from typing import List
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.constants.dtos import UserLoginAccessTokenDTO
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from auth_user.constants.exception_messeges import INVALID_PHONE_NUMBER, USER_DOES_NOT_EXISTS
from auth_user.constants.dtos import UserProfileDTO

class PresenterImplementation(PresenterInterface):

    def user_access_token(self, access_token: UserLoginAccessTokenDTO):
        access_token_dict = {
            "access_token": access_token.access_token,
            "user_id": access_token.user_id
        }
        response = json.dumps(access_token_dict)
        return HttpResponse(response)

    def raise_exception_for_invalid_phone_number(self):
        raise NotFound(*INVALID_PHONE_NUMBER)

    def raise_exception_for_user_does_not_exist(self):
        raise NotFound(*USER_DOES_NOT_EXISTS)

    def user_profile_dto_response(self, user_profile_dto: List[UserProfileDTO]):
        list_of_user_profiles = []
        for user in user_profile_dto:
            user_profile = {
                "name": user.username,
                "gender": user.gender,
                "email": user.email,
                "phone_number": user.phone_number,
                "image_url": user.image_url
            }
            list_of_user_profiles.append(user_profile)
        response = json.dumps(list_of_user_profiles)
        return HttpResponse(response)