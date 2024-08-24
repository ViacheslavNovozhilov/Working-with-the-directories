from unittest import TestCase

from CSV_logic import csv_read, check_login_exist
from config import Config


class RegistrationTest(TestCase):
    def setUp(self):
        self.config = Config(storage_path='test.csv')

    def tearDown(self):
        pass

    def test_csv_read(self):
        data = csv_read()
        self.assertEqual(type(data), list)
        self.assertEqual(type(data[0]), dict)

    def test_login_exist(self):
        exist_result = check_login_exist('test', 'test@mail.ru', self.config)
        self.assertTrue(exist_result)
        not_exist_result = check_login_exist('guest', 'test@mail.ru', self.config)
        self.assertFalse(not_exist_result)
