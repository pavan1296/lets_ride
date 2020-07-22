"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from auth_user.factory import UserFactory
from auth_user.models import User

REQUEST_BODY = """

"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["superuser"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01UserProfileAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def test_case(self):
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        # user = UserFactor()
        # print(user.id)

        response = self.default_test_case()
        import json
        response_content = json.loads(response.content)

        self.assert_match_snapshot(
            name="user_profile",
            value=response_content
        )