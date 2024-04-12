#!/usr/bin/env python3
"""A module for testing utils.access_nested_map function
"""
import unittest
from parameterized import parameterized


access_nested_map = __import__("utils").access_nested_map


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
