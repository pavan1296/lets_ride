"""
# TODO: Update test case description
"""
from unittest.mock import create_autospec, patch
from auth_user.interactors.user_login_interactor import UserLoginInteractor
from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from auth_user.factory import UserFactory
from auth_user.constants.dtos import UserLoginAccessTokenDTOFactoy
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from auth_user.models import User

REQUEST_BODY = """
{
    "phone_number": "7799888142",
    "password": "pavan"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase01UserLoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @patch.object(OAuthUserAuthTokensService, 'create_user_auth_tokens')
    def test_case(self, token_mock):
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        user = UserFactory.create()
        user.set_password('pavan')
        user.save()
        token_mock.return_value = UserLoginAccessTokenDTOFactoy
        response = self.default_test_case()
        import json
        response_content = json.loads(response.content)

        self.assert_match_snapshot(
            name="access_token",
            value=response_content
        )