# pylint: disable=wrong-import-position

APP_NAME = "auth_user"
OPERATION_NAME = "user_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/user_profile/v1/"

from .test_case_01 import TestCase01UserProfileAPITestCase

__all__ = [
    "TestCase01UserProfileAPITestCase"
]
