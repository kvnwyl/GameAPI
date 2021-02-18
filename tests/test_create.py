import unittest
import json

from http.client import HTTPConnection
from unittest.case import TestCase
from urllib.parse import urlencode


class TestCreate(unittest.TestCase):
    response = None
    response_read = None

    @classmethod
    def setUpClass(cls):
        """Custom setUp class to set class variables. This is to prevent
        unique constraint failures on SQLAlchemy from the POST requests
        being hit for each test method.
        """

        if not cls.response:
            base_url = "localhost"
            port = 8080

            # dictionary laid out in different format to make it easier on
            # the eyes.
            request_json = {
                "name":             "Sonic The Hedgehog",
                "region":           "PAL",
                "release_date":     "1991-06-21T00:00:00Z",
                "console":          "Megadrive",
                "series":           "Sonic",
                "genre":            "Platformer,Adventure",
                "tags":             "",
                "rating":           7,
                "developer":        "Sonic Team",
                "publisher":        "Sega",
                "play_count":       2,
                "last_played":      "2021-02-16T00:00:00Z",
                "play_duration":    240
            }

            headers = {"content-type": "application/json"}

            conn = HTTPConnection(base_url, port)
            conn.request("POST", "/game", json.dumps(request_json), headers)
            cls.response = conn.getresponse()
            cls.response_read = json.loads(cls.response.read().decode())

    def test_success(self):
        self.assertEqual(TestCreate.response.status, 200)

    def test_reason(self):
        self.assertEqual(TestCreate.response.reason, "OK")

    def test_return(self):
        self.assertEqual(type(TestCreate.response_read), dict)

    def test_return_code(self):
        self.assertEqual(TestCreate.response_read.get("status"), "200")

    def test_return_message(self):
        self.assertEqual(TestCreate.response_read.get("message"), "success")