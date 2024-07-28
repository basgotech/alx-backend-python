#!/usr/bin/env python3
"""Module containing  unit test for utils package"""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch
from utils import memoize


class TestAccessNestedMap(TestCase):
    """class that inherits from unittest.TestCase."""

    @parameterized.expand([({"a": 1}, ("a",), 1), ({"a": {
        "b": 2}}, ("a",), {"b": 2}), ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, res):
        """method to test that the method returns what it is supposed to."""

        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self,  nested_map, path):
        """context manager to test that a KeyError is raised for
        the following inputs
        """

        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(TestCase):
    """class and implement the TestGetJson.test_get_json"""

    @parameterized.expand([("http://example.com", {
        "payload": True}), ("http://holberton.io", {"payload": False})])
    @patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock):
        """method to test that utils.get_json returns the expected result"""

        mock.return_value = test_payload
        res_grapper = get_json(test_url)
        self.assertEqual(res_grapper, test_payload)


class TestMemoize(TestCase):
    """memoization and familiarize yourself with the utils.memoize"""

    def test_memoize(self):
        """Method that using test memorize to check if func is called twice"""

        class TestClass:
            """Class that defines attributes to test memoize"""

            def a_method(self):
                """Use unittest.mock.patch to mock a_method"""

                return 42

            @memoize
            def a_property(self):
                """Test that when calling a_property twice"""

                return self.a_method()

        with patch.object(TestClass, "a_method") as mock:
            test_f = TestClass()
            test_f.a_property
            test_f.a_property
            mock.assert_called_once
