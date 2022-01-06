import string
def rot13(message):
    dict_num_let = _make_dict_num_letter()
    dict_let_num = _make_dict_leter_num()
    new_word = ""
    for letter in message:
        if letter in "!?,.:;1234567890+-*/" or letter == " ":
            new_word += letter
        else:
            if letter == letter.upper():
                this_letter = letter.lower()
            else:
                this_letter = letter
            position = dict_let_num[this_letter]
            position += 13
            if position > 26: position -= 26
            if letter == letter.upper():
                new_word += dict_num_let[position].upper()
            else:
                new_word += dict_num_let[position]
    return new_word


def _make_dict_num_letter():
    dict_let_num = dict()
    n = 1
    for char in string.ascii_lowercase:
        dict_let_num[n] = char
        n += 1
    return dict_let_num

def _make_dict_leter_num():
    dict_let_num = dict()
    n = 1
    for char in string.ascii_lowercase:
        dict_let_num[char] = n
        n += 1
    return dict_let_num
