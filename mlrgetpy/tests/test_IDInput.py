import unittest
from mlrgetpy.IDInput import IDInput


class test_IDInput(unittest.TestCase):

    def test_str_json(self):
        id_input: IDInput = IDInput("739")
        result: str = id_input.str_json()
        expected = '{"0":{"json":"739"}}'
        self.assertEqual(expected, result)
