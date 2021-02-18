import unittest
import json

from http.client import HTTPConnection
from unittest.case import TestCase
from urllib.parse import urlencode


class TestDelete(unittest.TestCase):
    response = None
    response_read = None

    @classmethod
    def setUpClass(cls):

        if not cls.response:
            base_url = "localhost"
            port = 8080

            headers = {"content-type": "application/json"}

            conn = HTTPConnection(base_url, port)
            conn.request("DELETE","/game/id/1","",headers)
            cls.response = conn.getresponse()
            cls.response_read = json.loads(cls.response.read().decode())

    def test_delete_success(self):
        self.assertEqual(TestDelete.response.status, 200)

    def test_delete_reason(self):
        self.assertEqual(TestDelete.response.reason, "OK")

    def test_delete_return(self):
        self.assertEqual(type(TestDelete.response_read), dict)