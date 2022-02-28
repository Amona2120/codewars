def encrypt_this(text):
    a = ""
    for i in text.split():
        if len(i) > 2:
            a += str(ord(i[0])) + i[-1] + i[2:-1] + i[1] + " "
        if len(i) == 1:
            a += str(ord(i[0])) + " "
        if len(i) == 2:
            a += str(ord(i[0])) + i[1] + " "

    return a[:-1]
