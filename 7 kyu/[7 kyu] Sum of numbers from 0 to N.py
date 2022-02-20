def show_sequence(n):
    if n<0: return f"{n}<0"
    if n == 0: return "0=0"
    n = [i for i in range(n+1)]
    return "+".join(str(a) for a in n) + f" = {sum(i for i in n)}"
