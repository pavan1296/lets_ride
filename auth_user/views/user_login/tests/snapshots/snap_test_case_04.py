# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04UserLoginAPITestCase::test_case status'] = 400

snapshots['TestCase04UserLoginAPITestCase::test_case body'] = {
    'http_status_code': None,
    'res_status': 'USER_DOES_NOT_EXISTS',
    'response': 'You are not registered with us, please register'
}

snapshots['TestCase04UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '122',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots['TestCase04UserLoginAPITestCase::test_case access_token'] = {
    'http_status_code': None,
    'res_status': 'USER_DOES_NOT_EXISTS',
    'response': 'You are not registered with us, please register'
}
