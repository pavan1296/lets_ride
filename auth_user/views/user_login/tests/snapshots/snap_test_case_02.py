# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase::test_case status'] = 400

snapshots['TestCase02UserLoginAPITestCase::test_case body'] = {
    'http_status_code': None,
    'res_status': 'INVALID_PHONE_NUMBER',
    'response': 'You are giving invalid phone number or password please check again'
}

snapshots['TestCase02UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '141',
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

snapshots['TestCase02UserLoginAPITestCase::test_case access_token'] = {
    'http_status_code': None,
    'res_status': 'INVALID_PHONE_NUMBER',
    'response': 'You are giving invalid phone number or password please check again'
}
