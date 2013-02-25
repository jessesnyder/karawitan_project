"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
# from django.test import TestCase
from django_webtest import WebTest


class FunctionalTestCase(WebTest):

    def test_admin_enabled(self):
        response = self.app.get('/admin')
        self.assertEqual(u'', response.text)

    def test_musician_listing_exists(self):
        index = self.app.get('/musicians')
        assert 'Musicians' in index
