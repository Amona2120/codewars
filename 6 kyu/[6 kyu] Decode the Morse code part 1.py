def decodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[char] for char in word.split())
        for word in morse_code.strip().split('   '))
