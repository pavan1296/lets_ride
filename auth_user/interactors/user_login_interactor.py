import re
from auth_user.interactors.presenters.presenter_interface import PresenterInterface
from auth_user.interactors.storages.storage_interface import StorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from auth_user.exceptions.exceptions import InvalidPhonenumber, UserDoesNotExist
from auth_user.constants.dtos import UserLoginAccessTokenDTO

class UserLoginInteractor:
    def __init__(self, storage: StorageInterface, presenter: PresenterInterface, oauth2_storage: OAuth2SQLStorage):
        self.storage = storage
        self.presenter = presenter
        self.oauth2_storage = oauth2_storage

    def login_validation(self, phone_number: str, password: str):

        #TODO: check phone number exists in user
        #TODO: check phone number greater than 10 chars or less than 10 chars
        #TODO: Check phone number conains alphabets
        #TODO: check phone number startswith 7 or 8 or 9
        #TODO: check phone number contains special characters
        #TODO: check phone number and password exists in user
        try:
            access_token = self._check_user_credentials(phone_number=phone_number, password=password)
            return self.presenter.user_access_token(access_token=access_token)
        except InvalidPhonenumber:
            return self.presenter.raise_exception_for_invalid_phone_number()
        except UserDoesNotExist:
            return self.presenter.raise_exception_for_user_does_not_exist()


    def _check_user_credentials(self, phone_number: str, password: str):
        self._validate_phone_number(phone_number=phone_number)

        user_id = self._validate_phone_number_with_password(phone_number=phone_number, password=password)
        from common.oauth_user_auth_tokens_service import \
            OAuthUserAuthTokensService
        print(user_id)
        oauth = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth2_storage
        )

        access_token_dto = oauth.create_user_auth_tokens(user_id=user_id)
        access_token_with_user_id_dto = UserLoginAccessTokenDTO(
            access_token=access_token_dto.access_token,
            user_id=user_id
        )
        return access_token_with_user_id_dto

    def _validate_phone_number(self, phone_number: str):
        is_invalid_phone_number = not re.match(r'^([6-9])',phone_number)
        if is_invalid_phone_number:
            raise InvalidPhonenumber
        is_invalid_phone_number = len(phone_number) > 10 or len(phone_number) < 10
        if is_invalid_phone_number:
            raise InvalidPhonenumber
        is_invalid_phone_number = any(number.isalpha() for number in phone_number)
        if is_invalid_phone_number:
            raise InvalidPhonenumber
        is_invalid_phone_number = any(not c.isalnum() for c in phone_number)
        if is_invalid_phone_number:
            raise InvalidPhonenumber
        self.storage.check_phone_number_exists_in_user(phone_number=phone_number)

    def _validate_phone_number_with_password(self, phone_number: str, password: str):

        try:
            user_id = self.storage.check_phone_number_and_password_exists_in_user(
                    phone_number=phone_number, password=password
            )
            return user_id
        except UserDoesNotExist:
            raise UserDoesNotExist