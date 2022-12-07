from mlrgetpy.JsonParser import JsonParser
import unittest
import os


class TestJsonParser(unittest.TestCase):

    def test_encode(self):

        f = open('dataset.json', "r")
        json = f.read()
        f.close()

        # print(json)

        jsp = JsonParser()
        data = jsp.encode(json)

        datasets = data[0]["result"]["data"]["json"]["datasets"]
        self.assertEqual(datasets[0]["Name"],
                         "NATICUSdroid (Android Permissions) Dataset")
        self.assertEqual(datasets[1]["Name"],
                         "Bengali Hate Speech Detection Dataset")
