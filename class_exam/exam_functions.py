

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


def reaarange_list(u_name, u_list):
    i = u_list.index(u_name)
    u_list.insert(0, u_list.pop(i))
    return u_list