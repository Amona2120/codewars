def revrot(strng, sz):
    answer = ""
    while len(strng) >= sz and sz != 0:
        part = strng[:sz]
        if sum(int(a) for a in part)%2==0:
            answer += part[::-1]
        else:
            answer += part[1:] + part[0]
        strng = strng[sz:]
    return answer
