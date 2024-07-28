#!/usr/bin/env python3
"""memoize turns methods into properties"""
from unittest import TestCase
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
from unittest.mock import PropertyMock
from fixtures import TEST_PAYLOAD
from urllib.error import HTTPError
from parameterized import parameterized_class


class TestGithubOrgClient(TestCase):
    """"Class that test client.GithubOrgClient class"""

    @parameterized.expand([("google"), ("abc")])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock):
        """test that GithubOrgClient.org returns the correct value"""

        client_d = GithubOrgClient(org_name)
        res_graper = client_d.org

        self.assertEqual(res_graper, mock.return_value)
        mock.assert_called_once

    def test_public_repos_url(self):
        """method to unit-test GithubOrgClient._public_repos_url"""

        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock,
                          return_value={"repos_url": "Test value"}
                          ) as mock:
            test_json_file = {"repos_url": "Test value"}
            client_d = GithubOrgClient(test_json_file.get("repos_url"))
            res_graper = client_d._public_repos_url

            self.assertEqual(res_graper, mock.return_value.get("repos_url"))
            mock.assert_called_once

    @patch("client.get_json", return_value=[{"name": "Test value"}])
    def test_public_repos(self, mock):
        """to unit-test GithubOrgClient.public_repos."""

        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/"
                          ) as pub:
            client_d = GithubOrgClient("Test value")
            res_graper = client_d.public_repos()

            self.assertEqual(res_graper, ["Test value"])
            mock.assert_called_once
            pub.assert_called_once

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, license_key, ret):
        """to unit-test GithubOrgClient.has_license."""

        client_d = GithubOrgClient("Test value")
        res_graper = client_d.has_license(repo, license_key)
        self.assertEqual(ret, res_graper)


@parameterized_class(("org_payload", "repos_payload", "expected_repos",
                     "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(TestCase):
    """Class that defines attributes to test client.GithubOrgClient class"""

    @classmethod
    def setUpClass(cls):
        """mock requests.get to return example payloads"""

        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """class method to stop the patcher."""

        cls.get_patcher.stop()

    def test_public_repos(self):
        """method to unit-test GithubOrgClient._public_repos_url."""

        res_graper = GithubOrgClient("Test value")
        self.assertTrue(res_graper)
