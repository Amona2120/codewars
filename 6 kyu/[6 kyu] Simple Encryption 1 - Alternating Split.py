def decrypt(encrypted_text, n):
    if encrypted_text == None: return None
    if n <= 0: return encrypted_text
    else:
        second_part = encrypted_text[len(encrypted_text)//2:]
        first_part = encrypted_text[:len(encrypted_text)//2]
        answer = ""
        for i in range(len(second_part)):
                answer += second_part[i] + first_part[i:i+1]
        return decrypt(answer, n-1)


def encrypt(text, n):
    for _ in range(n):
        text = text[1::2]+text[::2]
    return text
