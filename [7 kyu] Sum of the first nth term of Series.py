def series_sum(n):
    if n == 0: return "0.00"
    arr = []
    b = 1
    for i in range(n):
        arr.append(1/b)
        b += 3
    return f"{round(sum(arr), 2)}" if str(round(sum(arr), 2))[-3]=="." else f"{round(sum(arr), 2)}0"

