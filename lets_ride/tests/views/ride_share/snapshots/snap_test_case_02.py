# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02RideShareAPITestCase.test_case status_code'] = '400'

snapshots['TestCase02RideShareAPITestCase.test_case body'] = {
    'http_status_code': None,
    'res_status': 'INVALID_ASSET_TYPE',
    'response': 'invalid asset type given'
}
