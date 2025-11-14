#!/usr/bin/env python3
import unittest
from parameterized import parameterized,assertRaises
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map using parameterized decorator."""
        self.assertEqual(access_nested_map(nested_map, path), expected)  
            
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

    # Verify the exception key message (Python formats KeyError as "'key'")
            self.assertEqual(str(context.exception), repr(path[-1]))