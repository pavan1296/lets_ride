"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from lets_ride.interactors.storages.dtos.dtos import RideRequestDTOFactory

REQUEST_BODY = """
{
    "from_place": "string",
    "to_place": "string",
    "is_flexible": true,
    "flexible_from_time": "2099-12-31 00:00:00",
    "flexible_to_time": "2099-12-31 00:00:00",
    "no_of_seats": 1,
    "luggage_quantity": 1,
    "travel_date_time": "2099-12-31 00:00:00"
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


class TestCase01RideRequestAPITestCase(CustomAPITestCase):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01RideRequestAPITestCase, self).setupUser(
            username=username, password=password
        )
        RideRequestDTOFactory()

    def test_case(self):
        # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.
        response = self.default_test_case()

        self.assert_match_snapshot(
            name="ride_request",
            value=response.status_code
        )