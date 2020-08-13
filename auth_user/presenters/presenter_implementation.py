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
        return HttpResponse(response, status=400)

    def raise_exception_for_user_does_not_exist(self):
        invalid_user = {
            "response": USER_DOES_NOT_EXISTS[0],
            "status": 400,
            "res_status": USER_DOES_NOT_EXISTS[1]
        }
        response = json.dumps(invalid_user)
        return HttpResponse(response, status=400)

    def user_profile_dto_response(self, user_profile_dto: UserProfileDTO):
        user_profile = {
                "name": user_profile_dto.username,
                "gender": user_profile_dto.gender,
                "email": user_profile_dto.email,
                "phone_number": user_profile_dto.phone_number,
                "image_url": user_profile_dto.image_url
        }
        response = json.dumps(user_profile)
        return HttpResponse(response)