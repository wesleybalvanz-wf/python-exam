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

