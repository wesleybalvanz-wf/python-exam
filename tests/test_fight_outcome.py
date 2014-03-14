import unittest
from class_exam.fight_outcome import UserStats
import mock

class TestUserStats(unittest.TestCase):
    def test_get_name(self):
        user = "User 1"
        self.assertEqual(UserStats(user).get_name(), user)

    def test_get_stats(self):
        user = "User 1"
        user_stats = UserStats(user).get_stats()
        self.assertTrue(user_stats >= 1)
        self.assertTrue(user_stats <= 10)

    def test_get_name_and_stats(self):
        user = "User 1"
        user_name, user_stats = UserStats(user).get_name_and_stats()
        self.assertEqual(user_name, user)
        self.assertTrue(user_stats >= 1)
        self.assertTrue(user_stats <= 10)
