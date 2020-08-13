# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetShareRideDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetShareRideDetailsAPITestCase.test_case body'] = [
    {
        'asset_quantity': 1,
        'date_and_time': 'string',
        'from_place': 'string',
        'no_of_seats': 1,
        'status': 'ACTIVE',
        'to_place': 'string'
    }
]
