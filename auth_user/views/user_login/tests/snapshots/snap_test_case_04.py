# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UserLoginAPITestCase::test_case status'] = 200

snapshots['TestCase04UserLoginAPITestCase::test_case body'] = {
    'res_status': 'USER_DOES_NOT_EXISTS',
    'response': 'You are not registered with us, please register',
    'status': 400
}

snapshots['TestCase04UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '116',
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

snapshots['TestCase04UserLoginAPITestCase::test_case access_token'] = {
    'res_status': 'USER_DOES_NOT_EXISTS',
    'response': 'You are not registered with us, please register',
    'status': 400
}
