import json
from django.db.utils import IntegrityError
from django.test import TestCase
from unittest import mock

from github.models import ProgrammingLanguage, Repository
from github.utils import get_github_repos


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_requests_get_success(*args, **kwargs):
    with open('github/supporting_files/github_success_response.json') as json_data:
        parsed_json = json.load(json_data)
        return MockResponse(parsed_json, 200)
    return MockResponse({}, 404)


def mocked_requests_get_error(*args, **kwargs):
    with open('github/supporting_files/github_error_response.json') as json_data:
        parsed_json = json.load(json_data)
        return MockResponse(parsed_json, 422)
    return MockResponse({}, 404)


class TestGithubUtils(TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get_success)
    def test_get_github_repos_with_success(self, *args):
        """
        The mocked function return an response from an static file located on
        supporting_files folder with the same response that the api returns
        on an success request. The list has 30 repositories.

        get_github_repos should retorn an list with 30 dicts
        """
        fetched_data = get_github_repos('python')

        self.assertTrue(isinstance(fetched_data, list))
        self.assertEqual(len(fetched_data), 30)

        first_elem = fetched_data[0]
        self.assertTrue(isinstance(first_elem, dict))

    @mock.patch('requests.get', side_effect=mocked_requests_get_error)
    def test_get_github_repos_with_error(self, *args):
        """
        The mocked function return an response from an static file located on
        supporting_files folder with the same response that the api returns
        on an error request.

        get_github_repos should retorn an empty list
        """
        fetched_data = get_github_repos('python')

        self.assertTrue(isinstance(fetched_data, list))
        self.assertEqual(len(fetched_data), 0)

    @mock.patch('requests.get', side_effect=mocked_requests_get_success)
    def test_repository_creation_after_new_language(self, *args):
        """
        After saving an ProgrammingLanguage object, should automatically
        search for respective repositories and save it.
        """
        ProgrammingLanguage.objects.create(name='python')
        repos = Repository.objects.filter(language__name='python')

        self.assertEqual(repos.count(), 30)

    @mock.patch('requests.get', side_effect=mocked_requests_get_success)
    def test_create_duplicated_programming_language(self, *args):
        """
        Should raise an IntegrityError when creating programming language with
        duplicated name.
        """
        ProgrammingLanguage.objects.create(name='python')

        with self.assertRaises(IntegrityError):
            ProgrammingLanguage.objects.create(name='python')
