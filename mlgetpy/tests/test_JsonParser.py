from mlgetpy.JsonParser import JsonParser
import unittest
import os

class TestJsonParser(unittest.TestCase):

    def test_encode(self):
        
        f = open('dataset.json', "r")
        json = f.read()
        f.close()

        #print(json)

        jsp = JsonParser()
        data = jsp.encode(json)

        self.assertEqual(data["payload"]["rows"][0]["Name"], "NATICUSdroid (Android Permissions) Dataset")
        self.assertEqual(data["payload"]["rows"][1]["Name"], "Bengali Hate Speech Detection Dataset")