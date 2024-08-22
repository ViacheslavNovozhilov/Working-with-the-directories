from unittest import TestCase
from CSV_logic import csv_read


class CSVRead(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_csv_read(self):
        self.assertEqual(type(csv_read()), list)
