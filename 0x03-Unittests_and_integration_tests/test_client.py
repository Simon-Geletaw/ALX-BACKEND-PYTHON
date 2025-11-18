#!/usr/bin/env python3

from client import GithubOrgClient
from unittest import patch
from parameterized import parameterized
import unittest


class TestGithubClient(unittest.TestCase):
    @parameterized.expand([("google",),
                           "abc",])
    @patch('client.get_json')
    def test_org(self, org, mock_test):
        mock_test.return_value = {"login": org}
        client = GithubOrgClient(org)
        result = client.org
        self.assertEqual(result, {"login": org})

        mock_test.assert_called_once_with(f"https://api.github.com/orgs/{org}")


if __name__ == '__main__':
    unittest.main()
