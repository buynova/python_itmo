import unittest
import json
import os
import sys
from homework.param_handler import param_handler


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello, Python!'

        self.assertEqual(s.split(), ['Hello,', 'Python!'])

        with self.assertRaises(TypeError):
            s.split(1)


class TestParamHandler(unittest.TestCase):
    def setUp(self):
        """Выполнение перед каждым тестом"""
        self.filename = 'config.json'
        self.data = {
            "key1": "value1",
            "key2": "value2"
        }

        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        """Выполнение перед каждым тестом"""
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_get_instance(self):
        ph = param_handler.ParamHandler.get_instance(self.filename)
        self.assertIsInstance(ph, param_handler.JsonParamHandler, msg='Вернулся не JsonParamHandler')

    def test_read(self):
        ph = param_handler.ParamHandler.get_instance(self.filename)
        ph.read()
        self.assertDictEqual(ph.get_all_params(), self.data)

        params = ph.get_all_params()
        self.assertIn('key3', params)
        self.assertIsInstance(params.get('key3'), bool)


class TestCustom(unittest.TestCase):
    @unittest.skipUnless(sys.platform.startswith('win'), 'Windows is required')
    def test_windows(self):
        pass

    def test_even(self):
        for i in range(5):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)


if __name__ == '__main__':
    unittest.main()
