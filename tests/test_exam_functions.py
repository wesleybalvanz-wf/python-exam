import unittest
from class_exam.exam_functions import read_list
from class_exam.exam_functions import list_from_file
from class_exam.exam_functions import rearrange_list
from class_exam.exam_functions import get_users
import mock
from mock import call


class TestListFromFile(unittest.TestCase):

    @mock.patch('__builtin__.open')
    def test_read_file(self, open_mock):
        user_list = ['user_1', 'user_2', 'user_3', 'user_4']
        file_list = ['user_1\n', 'user_2\n', 'user_3\n', 'user_4\n']
        open_mock.return_value = file_list
        output = list_from_file(open_mock)
        self.assertEqual(output, user_list)

    @mock.patch('__builtin__.open')
    def test_read_file_error(self, open_mock):
        open_mock.side_effect = IOError
        output = list_from_file(open_mock)
        self.assertEqual(output, "You're in the wrong directory.")


class TestReadList(unittest.TestCase):

    def setUp(self):
        self.list_of_users = ['user_1', 'user_2', 'user_3', 'user_4']

    @mock.patch('__builtin__.raw_input')
    @mock.patch('sys.stdout.write')
    def test_user_found(self, print_mock, raw_mock):
        raw_mock.return_value = 'user_2'
        output = read_list(self.list_of_users)
        print_mock.assert_has_calls([call("You're on the list."), call('\n')])
        self.assertEqual(output, ('user_2', True))
        self.assertEqual(print_mock.called, True)
        self.assertEqual(raw_mock.call_count, 1)
        self.assertEqual(print_mock.call_count, 2)

    @mock.patch('__builtin__.raw_input')
    @mock.patch('sys.stdout.write')
    def test_read_user_not_found(self, print_mock, raw_mock):
        raw_mock.return_value = 'user_5'
        output = read_list(self.list_of_users)
        print_mock.assert_has_calls([call("You're not on the list, user_5"),
                                     call('\n')])
        self.assertEqual(output, ('user_5', False))
        self.assertEqual(print_mock.called, True)
        self.assertEqual(raw_mock.call_count, 1)
        self.assertEqual(print_mock.call_count, 2)


class TestRearrangeList(unittest.TestCase):

    def test_rearrange_list(self):
        user_list = ['user_1', 'user_2', 'user_3', 'user_4']
        new_list = ['user_3', 'user_1', 'user_2', 'user_4']
        output = rearrange_list('user_3', user_list)
        self.assertEqual(output, new_list)


class TestGetUsers(unittest.TestCase):

    def test_get_users(self):
        user_name = 'user_1'
        user_list = ['user_1', 'user_2', 'user_3', 'user_4']
        opponent_list = ['user_2', 'user_3', 'user_4']
        opponents, user = get_users(user_name, user_list)
        self.assertEqual(user, 'user_1')
        self.assertEqual(opponents, opponent_list)