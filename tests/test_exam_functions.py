from class_exam.exam_functions import list_from_file, read_list, rearrange_list
from mock import call, patch
import unittest


class SetupList(unittest.TestCase):
    def setUp(self):
        self.user_list = ['user_1', 'user_2', 'user_3', 'user_4']


class TestListFromFile(SetupList):
    @patch('__builtin__.open')
    def test_read_file(self, open_mock):
        file_list = ['user_1\n', 'user_2\n', 'user_3\n', 'user_4\n']
        open_mock.return_value = file_list
        output = list_from_file(open_mock)
        self.assertEqual(output, self.user_list)

    @patch('__builtin__.open')
    def test_read_file_error(self, open_mock):
        open_mock.side_effect = IOError
        output = list_from_file(open_mock)
        self.assertEqual(output, "You're in the wrong directory.")


class TestReadList(SetupList):
    @patch('__builtin__.raw_input')
    @patch('sys.stdout.write')
    def test_user_found(self, print_mock, raw_mock):
        raw_mock.return_value = 'user_2'
        output = read_list(self.user_list)
        print_mock.assert_has_calls([call("You're on the list."), call('\n')])
        self.assertEqual(output, ('user_2', True))
        self.assertEqual(print_mock.called, True)
        self.assertEqual(raw_mock.call_count, 1)
        self.assertEqual(print_mock.call_count, 2)

    @patch('__builtin__.raw_input')
    @patch('sys.stdout.write')
    def test_read_user_not_found(self, print_mock, raw_mock):
        raw_mock.return_value = 'user_5'
        output = read_list(self.user_list)
        print_mock.assert_has_calls([call("You're not on the list, user_5"),
                                     call('\n')])
        self.assertEqual(output, ('user_5', False))
        self.assertEqual(print_mock.called, True)
        self.assertEqual(raw_mock.call_count, 1)
        self.assertEqual(print_mock.call_count, 2)


class TestRearrangeList(SetupList):
    def test_rearrange_list(self):
        new_list = ['user_3', 'user_1', 'user_2', 'user_4']
        output = rearrange_list('user_3', self.user_list)
        self.assertEqual(output, new_list)