"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from auth_user.factory import UserFactory
from auth_user.models import User

REQUEST_BODY = """
{
    "phone_number": "779988814r",
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


class TestCase02UserLoginAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def test_case(self):
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        user = UserFactory.create()
        user.set_password('pavan')
        user.save()
        response = self.default_test_case()
        import json
        response_content = json.loads(response.content)

        self.assert_match_snapshot(
            name="access_token",
            value=response_content
        )