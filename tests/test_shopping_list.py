from class_exam.shopping_list import ShoppingList
import unittest


class TestAddToList(unittest.TestCase):
    def setUp(self):
        l = ['Apples', 'Bananas', 'Oranges -Purchased', 'Watermelons']
        self.sample_list = ShoppingList(l)

    def test_item_in_list(self):
        result = self.sample_list.add_to_list("Apples")
        self.assertEqual(result, "Apples is already on the list!")

    def test_purchased_item_in_list(self):
        result = self.sample_list.add_to_list("Oranges")
        self.assertEqual(result, "You already bought Oranges.")

    def test_add_to_list(self):
        result = self.sample_list.add_to_list("Mangos")
        self.assertEqual(result, "Added Mangos to the list.")