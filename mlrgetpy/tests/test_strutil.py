import unittest
from mlrgetpy.util.Strutil import Strutil
from typing import List


class test_strutil(unittest.TestCase):

    def test_get_list(self):

        result: List = Strutil.get_list("computer, tabular", ",", 10)
        expected_result: List = ["computer,", "tabular"]
        self.assertListEqual(expected_result, result, "normal")

        result: List = Strutil.get_list("computer", ",", 10)
        expected_result: List = ["computer"]
        self.assertListEqual(expected_result, result, "short word")

        result: List = Strutil.get_list("Foo bar", ",", 10)
        expected_result: List = ["Foo bar"]
        self.assertListEqual(expected_result, result, "two short word")

        text = "long long long long text"
        expected_result = ["long long ", "long long ", "text"]
        result: List = Strutil.get_list(text, " ", 10)
        self.assertListEqual(expected_result, result, "long parragrahp")

        text = "longWorddd"
        expected_result = ["longWorddd"]
        result: List = Strutil.get_list(text, " ", 10)
        self.assertListEqual(expected_result, result)
        text = "longWorddddddddddddddddddddddddddd"
        expected_result = ["longWor..."]
        result: List = Strutil.get_list(text, " ", 10)
        self.assertListEqual(expected_result, result, "long word")

        text = "computer, long long long long text,tabular"
        result: List = Strutil.get_list(text, ",", 10)
        expected_result: List = ["computer,",
                                 "long long ",
                                 "long long ",
                                 "text,",
                                 "tabular"]
        self.assertListEqual(expected_result, result,
                             "long paragraph between commas")

        text = "computer, long long long long text,tabular long long long"
        result: List = Strutil.get_list(text, ",", 10)
        expected_result: List = ["computer,",
                                 "long long ",
                                 "long long ",
                                 "text,",
                                 "tabular ", "long long ", "long"]
        self.assertListEqual(expected_result, result,
                             "last element with long paragraph")

    def test_left(self):
        result = Strutil.left("jsbach_chorals_harmony.data", 18)
        expected = "jsbach_"
        self.assertEqual(expected, result)

        result = Strutil.left("jsbach_harmony.data", 18)
        expected = "jsbach_"
        self.assertEqual(expected, result)

    # @unittest.skip("skipped")
    def test_right(self):
        result = Strutil.right("jsbach_chorals_harmony.data", 18)
        expected = "y.data"
        self.assertEqual(expected, result)

        result = Strutil.right("jsbach_harmony.data", 18)
        expected = "y.data"
        self.assertEqual(expected, result)

    # @unittest.skip("skipped")
    def test_shorten(self):
        result = Strutil.shorten("jsbach_chorals_harmony.data", 18)
        expected = "jsbach_"'[...]'"y.data"
        self.assertEqual(expected, result)

        result = Strutil.shorten("jsbach_harmony.data", 18)
        expected = "jsbach_[...]y.data"
        self.assertEqual(expected, result)

        result = Strutil.shorten("jsbach_harmony.data", 18)
        expected = "jsbach_[...]y.data"
        self.assertEqual(expected, result)
