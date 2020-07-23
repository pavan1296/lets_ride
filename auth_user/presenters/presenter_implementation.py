import json
from typing import List
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.constants.dtos import UserLoginAccessTokenDTO
from django.http import HttpResponse
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
        invalid_phone_number_response = {
            "response": INVALID_PHONE_NUMBER[0],
            "status": 400,
            "res_status": INVALID_PHONE_NUMBER[1]
        }
        response = json.dumps(invalid_phone_number_response)
        return HttpResponse(response)

    def raise_exception_for_user_does_not_exist(self):
        invalid_user = {
            "response": USER_DOES_NOT_EXISTS[0],
            "status": 400,
            "res_status": USER_DOES_NOT_EXISTS[1]
        }
        response = json.dumps(invalid_user)
        return HttpResponse(response)

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