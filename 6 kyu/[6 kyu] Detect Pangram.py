import string

def is_pangram(s):
    a = "".join(i for i in sorted(s.lower()) if i.isalpha())
    b = ""
    for t in a:
        if t not in b:
            b += t
    return b == "abcdefghijklmnopqrstuvwxyz"
