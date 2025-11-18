#!/usr/bin/env python3

from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
import unittest


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([("google",),
                           "abc",])
    @patch('client.get_json')
    def test_org(self, org, mock_test):
        mock_test.return_value = {"login": org}
        client = GithubOrgClient(org)
        result = client.org
        self.assertEqual(result, {"login": org})

        mock_test.assert_called_once_with(f"https://api.github.com/orgs/{org}")

    def test_publuc_repos_url(self):
        org_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        client = GithubOrgClient("google")
        with patch.object(type(client),
                          'org',
                          new_callable=unittest.mock.PropertyMock) as mock_method:
            mock_method.return_value = org_payload
            result = client._public_repos_url
            self.assertEqual(result, org_payload["repos_url"])


if __name__ == '__main__':
    unittest.main()
