def data_reverse(data):
    a = []
    while len(data) > 0:
        n = data[-8:]
        del data[-8:]
        a += n
    return a
