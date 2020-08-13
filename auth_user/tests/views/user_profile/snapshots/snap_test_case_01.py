# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserProfileAPITestCase.test_case status_code'] = '500'

snapshots['TestCase01UserProfileAPITestCase.test_case body'] = {
    'gender': [
        '"" is not a valid choice.'
    ],
    'phone_number': [
        'This field may not be blank.'
    ]
}
