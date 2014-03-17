class ShoppingList():
    def __init__(self, items):
        self.items = items

    def show_list(self):
        list_width = max(len(s) for s in self.items)
        list_divider = "-" * (list_width + 2)
        print "My Shopping List:"
        print list_divider
        for item in self.items:
            item_len = len(item)
            space_diff = list_width - item_len
            spacing_before = " " * (space_diff/2)
            if (space_diff % 2) == 0:
                spacing_after = spacing_before
            else:
                spacing_after = " " * ((space_diff/2) + 1)
            print "|" + spacing_before + item + spacing_after + "|"
        print list_divider + "\n"

    def add_to_list(self, item):
        if item in self.items:
            return "%s is already on the list!" % item
        elif item + " -Purchased" in self.items:
            return "You already bought %s." % item
        else:
            self.items.append(item)
            return "Added %s to the list." % item

    def remove_from_list(self, item):
        if item in self.items:
            self.items.remove(item)
            return "%s has been removed from the list." % item
        elif item + " -Purchased" in self.items:
            return "You already bought %s." % item
        else:
            return "%s is not on the list." % item

    def purchase_item(self, purchased_item):
        if purchased_item in self.items:
            i = self.items.index(purchased_item)
            self.items[i] += " -Purchased"
            self.show_list()
            return "Purchased % s." % purchased_item
        elif purchased_item + " -Purchased" in self.items:
            return "You already bought %s." % purchased_item
        else:
            return "%s is not on your list!" % purchased_item