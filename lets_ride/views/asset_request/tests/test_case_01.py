"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from lets_ride.interactors.storages.dtos.dtos import AssetRequestDTOFactory


REQUEST_BODY = """
{
    "from_place": "string",
    "to_place": "string",
    "travel_date_time": "2099-12-31 00:00:00",
    "is_flexible": true,
    "flexible_from_time": "2099-12-31 00:00:00",
    "flexible_to_time": "2099-12-31 00:00:00",
    "no_of_assets": 1,
    "asset_type": "string",
    "asset_sensitivity": "NORMAL",
    "whom_to_deliver": "string"
}
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


class TestCase01AssetRequestAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01AssetRequestAPITestCase, self).setupUser(
            username=username, password=password
        )
        AssetRequestDTOFactory()

    def test_case(self):
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        response = self.default_test_case()

        self.assert_match_snapshot(
            name="asset_request",
            value=response.status_code
        )