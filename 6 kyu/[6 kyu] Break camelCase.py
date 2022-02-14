def solution(s):
    return "".join(" " + i if i == i.upper() else i for i in s)
