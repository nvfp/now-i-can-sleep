import unittest
from unittest.mock import patch

import os
import shutil
import tempfile
from io import StringIO


from nics.main.cmd_init.ensure_nics_env_can_be_installed import ensure_nics_env_can_be_installed

class TestEnsureNicsEnvCanBeInstalled(unittest.TestCase):

    def setUp(self):
        self.cwd = tempfile.mkdtemp()  # Create a temp dir
        self.container = 'test_container'

    def tearDown(self):
        ## Delete the temp dir
        shutil.rmtree(self.cwd)

    def test_existing_rebuild_docs_yml(self):

        file_path = os.path.join(self.cwd, '.github', 'workflows', 'rebuild-docs.yml')

        ## Create the .github/workflows/ folders
        os.makedirs(os.path.dirname(file_path))
        ## Create an empty rebuild-docs.yml
        open(file_path, 'w').close()

        ## Call the function and check that it exits with an error message
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit) as cm:
                ensure_nics_env_can_be_installed(self.cwd, self.container)
        self.assertEqual(cm.exception.code, 1)
        expected_msg = f'Cannot initialize NICS. This file already exists: {repr(file_path)}.'
        self.assertEqual(fake_out.getvalue().strip(), expected_msg)

    def test_existing_container_dir(self):

        ## Create a container directory
        container_dir = os.path.join(self.cwd, self.container)
        os.makedirs(container_dir)

        ## Call the function and check that it exits with an error message
        with patch('sys.stdout', new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit) as cm:
                ensure_nics_env_can_be_installed(self.cwd, self.container)
        self.assertEqual(cm.exception.code, 1)
        expected_msg = f'Cannot initialize NICS. This folder already exists: {repr(container_dir)}.'
        self.assertEqual(fake_out.getvalue().strip(), expected_msg)

    def test_no_exit(self):
        ## Call the function and check that it does not exit
        ensure_nics_env_can_be_installed(self.cwd, self.container)


# from nics.main.cmd_init.get_user_details import get_user_details

# class TestGetUserDetails(unittest.TestCase):

#     @patch('builtins.input', side_effect=['John', '25', ''])
#     def test_get_user_details(self, mock_input):
#         expected_details = {
#             'name': 'John',
#             'age': '25',
#         }
#         actual_details = get_user_details()
#         self.assertEqual(actual_details, expected_details)


if __name__ == '__main__':
    unittest.main()