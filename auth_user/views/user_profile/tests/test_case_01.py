"""
# TODO: Update test case description
"""
import pytest
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from django_swagger_utils.utils.test_utils import TestUtils


class TestCase01UserProfileAPITestCase(TestUtils):
        APP_NAME = APP_NAME
        OPERATION_NAME = OPERATION_NAME
        REQUEST_METHOD = REQUEST_METHOD
        URL_SUFFIX = URL_SUFFIX
        SECURITY = {'oauth': {'scopes': ['superuser']}}

        @pytest.mark.django_db
        def test_case(self, snapshot):
            body = {}
            path_params = {}
            query_params = {}
            headers = {}
            response = self.make_api_call(body=body,
                                          path_params=path_params,
                                          query_params=query_params,
                                          headers=headers,
                                          snapshot=snapshot)
