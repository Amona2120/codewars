def create_phone_number(n):
    number = list(map(lambda x: str(x), n))
    number.insert(0, "(")
    number.insert(4, ") ")
    number.insert(8, "-")
    return ''.join(number)
