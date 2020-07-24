"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01RideRequestAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'from_place': 'string',
            'to_place': 'string',
            'is_flexible': True,
            'flexible_from_time': '2099-12-31 00:00:00',
            'flexible_to_time': '2099-12-31 00:00:00',
            'no_of_seats': 1,
            'luggage_quantity': 1,
            'travel_date_time': '2099-12-31 00:00:00'
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
