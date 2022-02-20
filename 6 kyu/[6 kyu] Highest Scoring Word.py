d = "0abcdefghijklmnopqrstuvwxyz"

def high(x):
    largest_num, answer = 0, ""
    for word in x.split():
        a = 0
        for letter in word:
            a += d.index(letter)
        if a > largest_num:
            answer, largest_num = word, a
    return answer
