import unittest
from mlrgetpy.FilterInput import FilterInput
from mlrgetpy.enums.Area import Area
from typing import List


class TestFilter(unittest.TestCase):

    def test_str_json(self):

        filter_input = FilterInput(take=700)
        result = filter_input.str_json()
        expected = '{"0":{"json":{"Area":[],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":700}}}'
        self.assertEqual(expected, result)

        filter_input = FilterInput(area=["Computer"], take=20)
        result = filter_input.str_json()
        expected = '{"0":{"json":{"Area":["Computer"],"Keywords":[],"orderBy":"NumHits","sort":"desc","skip":0,"take":20}}}'
        self.assertEqual(expected, result)

        filter_input = FilterInput(area=["Computer"], keywords=[
                                   "key1", "key2"], order_by="NumHits", sort="asc", skip=1, take=50)
        result = filter_input.str_json()
        expected = '{"0":{"json":{"Area":["Computer"],"Keywords":["key1","key2"],"orderBy":"NumHits","sort":"asc","skip":1,"take":50}}}'
        self.assertEqual(expected, result)

    def test_constructor(self):

        with self.assertRaises(ValueError, msg="Must be an list of str"):
            FilterInput(area="Computer")

        with self.assertRaises(ValueError, msg="Must be an list of str"):
            FilterInput(keywords="key2")
