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
