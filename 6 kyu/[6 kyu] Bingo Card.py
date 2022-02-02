from random import randrange

def _get_numbers():
    numbers = []
    start, stop= 1, 16
    for u in range(5):
        for i in range(5):
            d = randrange(start,stop)
            while d in numbers:
                d = randrange(start,stop)
            numbers.append(d)
        start += 15
        stop += 15
    del numbers[12]
    return numbers

def _get_letters():
    return (("B," * 5) + ("I,"*5) + ("N,"*4) + ("G,"*5) + ("O,"*5)[:-1]).split(",")


def get_bingo_card():
    numbers = _get_numbers()
    letters = _get_letters()
    answer = []
    for i in range(24):
        answer.append(str(letters[i])+str(numbers[i]))
    return answer
