from class_exam.shopping_list import ShoppingList
import unittest
import mock


class SetupList(unittest.TestCase):
    def setUp(self):
        l = ['Apples', 'Bananas', 'Oranges -Purchased', 'Watermelons']
        self.sample_list = ShoppingList(l)


class TestAddToList(SetupList):
    def test_item_in_list(self):
        result = self.sample_list.add_to_list("Apples")
        self.assertEqual(result, "Apples is already on the list!")

    def test_purchased_item_in_list(self):
        result = self.sample_list.add_to_list("Oranges")
        self.assertEqual(result, "You already bought Oranges.")

    def test_add_to_list(self):
        result = self.sample_list.add_to_list("Mangos")
        self.assertEqual(result, "Added Mangos to the list.")


class TestRemoveFromList(SetupList):
    def test_remove_item(self):
        result = self.sample_list.remove_from_list("Apples")
        self.assertEqual(result, "Apples has been removed from the list.")

    def test_purchased_item(self):
        result = self.sample_list.remove_from_list("Oranges")
        self.assertEqual(result, "You already bought Oranges.")

    def test_not_on_list(self):
        result = self.sample_list.remove_from_list("Kiwi")
        self.assertEqual(result, "Kiwi is not on the list.")


class TestPurchaseItem(SetupList):
    def setUp(self):
        super(TestPurchaseItem, self).setUp()
        self.show_mock = mock.patch.object(ShoppingList, 'show_list').start()

    def test_purchase_item(self):
        result = self.sample_list.purchase_item("Watermelons")
        self.assertEqual(result, "Purchased Watermelons.")
        self.assertEqual(self.show_mock.call_count, 1)

    def test_purchased_item(self):
        result = self.sample_list.purchase_item("Oranges")
        self.assertEqual(result, "You already bought Oranges.")
        self.assertEqual(self.show_mock.call_count, 0)

    def test_not_on_list(self):
        result = self.sample_list.purchase_item("Strawberries")
        self.assertEqual(result, "Strawberries is not on your list!")
        self.assertEqual(self.show_mock.call_count, 0)