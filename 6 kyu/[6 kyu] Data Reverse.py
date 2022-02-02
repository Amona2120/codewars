def data_reverse(data):
    a = []
    while len(data) > 0:
        a += data[-8:]
        del data[-8:]
    return a
