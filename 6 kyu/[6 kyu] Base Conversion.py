def _to_num(string, c):
    return sum(c.index(string[::-1][i]) * len(c)**i for i in range(len(string)))

def _to_res(num, cc):
    if num == 0: return cc[0]
    string = ""
    while num > 0:
        string += cc[num % len(cc)]
        num = num // len(cc)
    return string[::-1]

def convert(input, source, target):
    return _to_res(_to_num(input, source), target)
