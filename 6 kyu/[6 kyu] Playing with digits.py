def dig_pow(n, p):
    arr = [int(i) for i in str(n)]
    new_arr = []
    for e in arr:
        new_arr.append(e**p)
        p += 1
    if sum(new_arr) % n == 0: return sum(new_arr)//n
    return -1
