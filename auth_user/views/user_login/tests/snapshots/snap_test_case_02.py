# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase::test_case status'] = 404

snapshots['TestCase02UserLoginAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_PHONE_NUMBER',
    'response': 'You are giving invalid phone number or password please check again'
}

snapshots['TestCase02UserLoginAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '145',
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

snapshots['TestCase02UserLoginAPITestCase::test_case access_token'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_PHONE_NUMBER',
    'response': 'You are giving invalid phone number or password please check again'
}
