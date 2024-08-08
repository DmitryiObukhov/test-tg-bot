import unittest
from unittest.mock import patch, Mock

from api import get_user_info


class TestAPI(unittest.TestCase):

    def test_get_user_info_context_manager(self):
        expected = {'login': 'test'}
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = expected

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = response_mock

            assert get_user_info('test') == expected
            assert mock_requests.get.call_count == 1

    def test_get_user_info_context_manager_github_error(self):
        error_response_mock = Mock()
        error_response_mock.status_code = 404

        with patch('api.requests') as mock_requests:
            mock_requests.get.return_value = error_response_mock
            result = get_user_info('test')
            self.assertEqual(result, {'Error': True, 'status_code': 404})
            assert mock_requests.get.call_count == 1


if __name__ == '__main__':
    unittest.main()
