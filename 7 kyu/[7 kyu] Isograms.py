def is_isogram(string):
    list_of_letters = list(map(lambda x: str(x), string.lower()))
    unique_list = list(set(list_of_letters))
    unique_list.sort()
    list_of_letters.sort()
    if len(unique_list) == len(list_of_letters) and unique_list == list_of_letters:
        return True
    return False
