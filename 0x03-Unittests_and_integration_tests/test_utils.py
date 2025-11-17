#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


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
        

class TestGetJson(unittest.TestCase):
    @parameterized.expand([ 
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
            ]) 
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock):
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock.return_value = mock_response
        
        json_data = get_json(test_url)
        mock.assert_called_with(test_url)
        self.assertEqual(json_data, test_payload)
                
    
if __name__ == '__main__':
    unittest.main()