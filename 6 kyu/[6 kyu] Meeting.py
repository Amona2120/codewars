def meeting(s):
    new_list = []
    str_with_friends = ""

    for name in s.replace(":", " ").split(";"):
        first_name, last_name = name.split()[0], name.split()[1]
        new_list.append(last_name.upper() + " " + first_name.upper())

    new_list.sort()

    for friend in new_list:
        last_name, name = friend.split()[0], friend.split()[1]
        str_with_friends += "(" + last_name + ", " + name + ")"
    return str_with_friends
