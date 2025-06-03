#!/usr/bin/python3
"""
Unit testing utilities
"""

import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as error_context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error_context.exception), f"'{path[-1]}'")

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        with patch("Unittests_and_integration_tests.utils.requests.get",
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
