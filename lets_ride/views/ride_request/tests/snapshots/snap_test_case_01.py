# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01RideRequestAPITestCase::test_case status'] = 201

snapshots['TestCase01RideRequestAPITestCase::test_case body'] = b''

snapshots['TestCase01RideRequestAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01RideRequestAPITestCase::test_case ride_request'] = 201

snapshots['TestCase01RideRequestAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01RideRequestAPITestCase.test_case body'] = b''
