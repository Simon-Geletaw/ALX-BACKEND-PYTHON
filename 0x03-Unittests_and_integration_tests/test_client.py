#!/usr/bin/env python3

from client import GithubOrgClient
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from unittest import TestCase
import unittest
from fixture import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([("google", ),
                           "abc", ])
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
                          unittest.mock.PropertyMock) as mock_method:
            mock_method.return_value = org_payload
            result = client._public_repos_url
            self.assertEqual(result, org_payload["repos_url"])

    @patch("client.get_json")  # patch get_json as a decorator
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos returns
        the expected list of repo names"""

        # Fake payload returned by get_json
        fake_repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        mock_get_json.return_value = fake_repos_payload

        client = GithubOrgClient("google")

        # Patch the _public_repos_url property
        with patch.object(
            type(client),
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_repos_url:
            url = "https://api.github.com/orgs/google/repos"
            mock_repos_url.return_value = url

            result = client.public_repos()

            expected = ["repo1", "repo2"]
            self.assertEqual(result, expected)

            # Ensure _public_repos_url was accessed exactly once
            mock_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license", }}, "my_license", True),
        ({"license": {"key": "other_license"}}, ("my_license"), False)])
    def test_has_license(self, license, license_key, output):

        client = GithubOrgClient("google")
        result = client.has_license(license, license_key)
        self.assertEqual(result, output)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Start patcher for requests.get and return fixture payloads."""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        # Configure .json() return values based on the ORDER of calls
        # GithubOrgClient will call:
        #   requests.get("https://api.github.com/orgs/<org>")
        #   requests.get("<repos_url from the above response>")
        mock_get.return_value = Mock()
        mock_get.return_value.json.side_effect = [
            cls.org_payload,       # First call: org info
            cls.repos_payload      # Second call: repos list
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop patcher for requests.get."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repos list."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test filtering repos by license."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
