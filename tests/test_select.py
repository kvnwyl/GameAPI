import unittest
import json

from http.client import HTTPConnection
from unittest.case import TestCase
from urllib.parse import urlencode


class TestSelect(unittest.TestCase):
    """
    Notes
        Only a select few methods are tested for selection as they
        use as other selection routes use the same shared method.
    """

    base_url = "localhost"
    port = 8080

    def test_count_success(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/count","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.status, 200)

    def test_count_reason(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/count","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.reason, "OK")

    def test_count_return(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/count","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(type(response_read), dict)

    def test_id_success(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/id/1","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.status, 200)

    def test_id_reason(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/id/1","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.reason, "OK")

    def test_id_return(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/id/1","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(type(response_read), dict)

    def test_favourite_success(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/favourite","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.status, 200)

    def test_favoutite_reason(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/favourite","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(response.reason, "OK")

    def test_favourite_return(self):
        headers = {"content-type": "application/json"}

        conn = HTTPConnection(
            TestSelect.base_url,
            TestSelect.port
            )
        conn.request("GET","/game/favourite","",headers)
        response = conn.getresponse()
        response_read = json.loads(response.read().decode())

        self.assertEqual(type(response_read), dict)