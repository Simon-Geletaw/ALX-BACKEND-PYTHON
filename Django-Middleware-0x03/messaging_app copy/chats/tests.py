from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from http import HTTPStatus
from messaging_app.middleware.ip_black_list import Ipblacklistmiddleware
from unittest.mock import patch
import unittest


class ipblacklistmiddlewareTests(TestCase):
    def setUp(self):
        self.client = self.client_class()
        
    def test_request_success_without_blacklist_setting(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
       
        
# Create your tests here.
