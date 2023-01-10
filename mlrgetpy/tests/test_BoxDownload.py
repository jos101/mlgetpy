import unittest
from mlrgetpy.BoxDownload import BoxDownload


class test_BoxDownload(unittest.TestCase):

    def test_top(self):
        bod = BoxDownload(92, False)

        result = bod.top()
        expected = "┌──────────────────────────────────────────────────────────────────────────────────────────┐"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.top()
        expected = "┌────────────────────────────────────────────────────────────────────┐"
        self.assertEqual(expected, result)

    def test_bottom(self):
        bod = BoxDownload(92, False)
        result = bod.bottom()
        expected = "└──────────────────────────────────────────────────────────────────────────────────────────┘"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.bottom()
        expected = "└────────────────────────────────────────────────────────────────────┘"
        self.assertEqual(expected, result)

    def test_header(self):
        bod = BoxDownload(92, False)
        result = bod.header("Hello World!")
        expected = "│Hello World!                                                                              │"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.header("Hello World!")
        expected = "│Hello World!                                                        │"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.header(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor")
        expected = """│Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do     │
│eiusmod tempor                                                      │"""
        self.assertEqual(expected, result, "header is printed in two rows")

    def test_row_sep(self):
        bod = BoxDownload(92, False)
        result = bod.row_sep()
        expected = "├──────────────────────────────────────────────────────────────────────────────────────────┤"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.row_sep()
        expected = "├────────────────────────────────────────────────────────────────────┤"
        self.assertEqual(expected, result)

    def test_text_row(self):
        bod = BoxDownload(92, False)
        result = bod.text_row("Hello World!")
        expected = "│Hello World!                                                                              │"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.text_row("Hello World!")
        expected = "│Hello World!                                                        │"
        self.assertEqual(expected, result)

    def test_download_row(self):
        tree = "└──"
        file = 'Iris.data'
        str_progress = "1054 Bytes"
        perc = 0.5

        bod = BoxDownload(92, False)
        result = bod.download_row(tree, file, str_progress, perc)
        expected = "│└──Iris.data                        1054 Bytes        [━━━━━━━━━━━━             ]50%      │"
        self.assertEqual(expected, result)

        bod = BoxDownload(70, False)
        result = bod.download_row(tree, file, str_progress, perc)
        expected = "│└──Iris.data               1054 Bytes    [━━━━━━━━━         ]50%    │"
        self.assertEqual(expected, result)

    def test_progress_bar(self):
        bod = BoxDownload(70, False)
        result = bod.progress_bar(0.6, 15)
        expected = "[━━━━━━━━     ]"

        self.assertEqual(expected, result)

    def test_download_row2(self):
        bod = BoxDownload(70, False)
        result = bod.download_row2("│", "ft.csv")
        expected = "││ft.csv                                                             │"
        self.assertEqual(expected, result)

        result = bod.download_row2(
            "│", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod")
        expected = """││Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do    │
│ eiusmod                                                            │"""
        self.assertEqual(expected, result, "Add one space in the second line")

        result = bod.download_row2(
            "├──", "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod")
        expected = """│├──Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do  │
│   eiusmod                                                          │"""
        self.assertEqual(expected, result, "Add 3 spaces in the second line")

    def test_box_download_row3(self):
        bod = BoxDownload(70, False)
        result = bod.download_row3(
            "Class aptent taciti",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
            7)
        expected = """│Class  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed │
│aptent do eiusmod tempor incididunt ut labore et dolore magna       │
│taciti aliqua. Ut enim ad minim veniam, quis nostrud exercitation   │
│       ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis│
│       aute irure dolor in reprehenderit in voluptate velit esse    │
│       cillum dolore eu fugiat nulla pariatur.                      │"""

        msg = "Left part has less rows than the right part"
        self.assertEqual(expected, result)

        result = bod.download_row3(
            "Class aptent taciti",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt.",
            7)

        expected = """│Class  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed │
│aptent do eiusmod tempor incididunt.                                │
│taciti                                                              │"""

        msg = "Left part has more rows than the right part"
        self.assertEqual(expected, result, msg)
