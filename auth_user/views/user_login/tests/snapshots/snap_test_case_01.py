# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserLoginAPITestCase::test_case status'] = 200

snapshots['TestCase01UserLoginAPITestCase::test_case body'] = {
    'access_token': 'DyRngpHdOSdrsiI12g12',
    'user_id': 1
}

snapshots['TestCase01UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '54',
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

snapshots['TestCase01UserLoginAPITestCase::test_case access_token'] = {
    'access_token': 'DyRngpHdOSdrsiI12g12',
    'user_id': 1
}
