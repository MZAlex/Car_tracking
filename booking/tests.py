# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase, Client

class StatusTest(TestCase):
    def setUp(self):
        self.client
        
    def test_public(self):
        urls = [{'url':'/accounts/login','status':200},
                {'url':'/accounts/logout/','status':302},
                {'url':'/accounts/profile/','status':302}
                ]
        for elem in urls:
            response = self.client.get(elem['url'])
            self.assertEqual(response.status_code, elem['status'])
# Create your tests here.
