def add(num1, num2):
    list1 = list(map(int, str(num1)))
    list2 = list(map(int, str(num2)))
    if num1 > num2:
        while len(list2) != len(list1): list2.insert(0, 0)
    if num1 < num2:
        while len(list2) != len(list1): list1.insert(0, 0)
    c = [int(x) + int(y) for x, y in zip(list1[::-1], list2[::-1])][::-1]
    e = [str(i) for i in c]
    return int("".join(e))
