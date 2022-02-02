def delete_nth(order,max_e):
    new_list = []
    for i in order:
        if max_e > new_list.count(i):
            new_list.append(i)
    return new_list
