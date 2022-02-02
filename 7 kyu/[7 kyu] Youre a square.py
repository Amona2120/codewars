def is_square(n):
    if n < 0:
        return False
    return round(n ** 0.5) ** 2 == n
