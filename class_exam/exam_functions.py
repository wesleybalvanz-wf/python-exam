

def list_from_file(file_name):
    user_list = []
    try:
        for line in open(file_name, 'r'):
            person = line.strip('\n')
            user_list.append(person)
    except IOError:
        return "You're in the wrong directory."
    return user_list


def read_list(users):
    user_name = raw_input("Enter your name: ")
    if user_name in users:
        print "You're on the list."
        return user_name, True
    else:
        print "You're not on the list, %s" % user_name
        return user_name, False


def rearrange_list(u_name, u_list):
    """

    @param u_name: Name of person to bring to front of list
    @param u_list: List of people
    @return: Rearranged list of people with u_name in front
    """
    i = u_list.index(u_name)
    u_list.insert(0, u_list.pop(i))
    return u_list


def modify_list(u_list):
    u_input = raw_input("Would you like to add or remove a user? ").lower()
    if u_input == "add":
        n_input = raw_input("Enter a name to add: ")
        u_list.append(n_input)
    elif u_input == "remove":
        try:
            n_input = raw_input("Enter a name to remove: ")
            u_list.remove(n_input)
        except ValueError:
            return "Specified user did not exist!"
    else:
        return "Invalid command, please type 'add' or 'remove'"
    return u_list


class ShoppingList():
    def __init__(self, items):
        self.items = items

    def show_list(self):
        longest_item = max(self.items)
        list_width = len(longest_item)
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
                spacing_after = " " * ((space_diff/2) +1)
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
            return self.items
        elif purchased_item + " -Purchased" in self.items:
            return "You already bought %s." % purchased_item
        else:
            return "%s is not on your list!" % purchased_item
