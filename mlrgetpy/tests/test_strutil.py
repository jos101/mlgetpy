import unittest
from mlrgetpy.util.Strutil import Strutil
from typing import List


class test_strutil(unittest.TestCase):

    def test_get_list(self):

        result: List = Strutil.get_list("computer, tabular", ",", 10)
        expected_result: List = ["computer", ", tabular"]
        self.assertListEqual(expected_result, result, "normal")

        result: List = Strutil.get_list("computer", ",", 10)
        expected_result: List = ["computer"]
        self.assertListEqual(expected_result, result, "short word")

        result: List = Strutil.get_list("Foo bar", ",", 10)
        expected_result: List = ["Foo bar"]
        self.assertListEqual(expected_result, result, "two short word")

        text = "long long long long text"
        expected_result = ["long long", " long long", " text"]
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

        #text = "computer, long long long long text,tabular"
        #result: List = Strutil.get_list(text, ",", 10)
        # expected_result: List = ["computer",
        #                         ", long",
        #                         " long long",
        #                         " long text",
        #                         ",tabular"]
