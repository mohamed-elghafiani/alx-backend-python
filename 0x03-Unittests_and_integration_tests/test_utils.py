#!/usr/bin/env python3
"""A module for testing utils.access_nested_map function
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch


access_nested_map = __import__("utils").access_nested_map
get_json = __import__("utils").get_json


class TestAccessNestedMap(unittest.TestCase):
    """unit tests for utils.access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test that a KeyError is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """unit tests for utils.get_json function
    """
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """test that the method returns what it supposed to
        """
        test_cases = [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
        for (test_url, test_payload) in test_cases:
            mock_get.return_value = Mock(json=Mock(return_value=test_payload))
            result = get_json(test_url)

            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)
            mock_get.reset_mock()
