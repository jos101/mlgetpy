from mlrgetpy.log.NormalLog import NormalLog
import unittest
from unittest.mock import patch
from io import StringIO


class test_NormalLog(unittest.TestCase):

    def test_write_url(self):

        normal_log = NormalLog()
        expected = "Opening http://localhost\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            normal_log.write_url('http://localhost')
            self.assertEqual(expected, fake_out.getvalue())

    def test_write_id(self):

        normal_log = NormalLog()
        expected = "id: 14\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            normal_log.write_id("14")
            self.assertEqual(expected, fake_out.getvalue())

    def test_write_use_cache(self):

        normal_log = NormalLog()
        expected = "using cache\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            normal_log.write_use_cache()
            self.assertEqual(expected, fake_out.getvalue())

    def test_write_add_ids(self):

        normal_log = NormalLog()
        expected = "adding IDs [12, 53, 55]\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            normal_log.write_add_ids([12, 53, 55])
            self.assertEqual(expected, fake_out.getvalue())

    def test_remove_indexes(self):

        normal_log = NormalLog()
        expected = "removing indexes [12, 53, 55]\n"

        with patch('sys.stdout', new=StringIO()) as fake_out:
            normal_log.write_remove_indexes([12, 53, 55])
            self.assertEqual(expected, fake_out.getvalue())
