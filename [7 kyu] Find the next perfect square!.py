import math

def find_next_square(sq):
    return ((sq**0.5)+1)**2 if math.isqrt(sq)**2==sq else -1
