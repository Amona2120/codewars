def expanded_form(num):
    answer = []
    a = 1
    str = ""
    while num > 0:
        answer.append((num%10)*a)
        a *= 10
        num //= 10
    answer = answer[::-1]
    for i in answer:
        if i != 0:
            str += f"{i} + "
    return str[:-3]
