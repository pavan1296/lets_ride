# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserProfileAPITestCase::test_case status'] = 200

snapshots['TestCase01UserProfileAPITestCase::test_case body'] = [
    {
        'email': 'username@user.com',
        'gender': '',
        'image_url': '',
        'name': 'username',
        'phone_number': ''
    }
]

snapshots['TestCase01UserProfileAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '103',
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

snapshots['TestCase01UserProfileAPITestCase::test_case user_profile'] = [
    {
        'email': 'username@user.com',
        'gender': '',
        'image_url': '',
        'name': 'username',
        'phone_number': ''
    }
]
