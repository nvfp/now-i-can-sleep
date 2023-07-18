import unittest
from unittest.mock import patch

from nics.main.cmd_init.get_user_details import get_user_details


class TestGetUserDetails(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', '25', 'Foo'])
    def test_get_user_details(self, mock_input):
        expected_details = {
            'name': 'John',
            'age': '25',
            'food': 'Foo'
        }
        actual_details = get_user_details()
        self.assertEqual(actual_details, expected_details)


if __name__ == '__main__':
    unittest.main()