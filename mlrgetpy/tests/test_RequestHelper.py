import unittest
from mlrgetpy.RequestHelper import RequestHelper


class TestRquestHelper(unittest.TestCase):

    def test_get(self):
        req: RequestHelper = RequestHelper()

        with self.assertRaises(ValueError, msg="Must be a json header"):
            req.get("http://www.google.com")

        with self.assertRaises(ValueError, msg="Error 404"):
            req.get("127.0.0.12:3000")
