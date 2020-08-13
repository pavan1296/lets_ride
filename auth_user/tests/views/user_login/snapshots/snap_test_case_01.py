# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UserLoginAPITestCase.test_case body'] = {
    'http_status_code': None,
    'res_status': 'INVALID_PHONE_NUMBER',
    'response': 'You are giving invalid phone number or password please check again'
}
