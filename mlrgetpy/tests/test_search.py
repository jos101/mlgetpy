from mlrgetpy import search
import unittest

class TestSearch(unittest.TestCase):

    def test_search(self):
        self.assertEqual(search(), 'searching...') 
        #self.assertEqual(search(), 'searching...') 
        #self.assertEqual(search(), 'searching...') 