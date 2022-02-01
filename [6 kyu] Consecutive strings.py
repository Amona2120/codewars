def longest_consec(strarr, k):
    if len(strarr) == 0 or k <= 0: return ""
    max_str = ""
    for i in range(len(strarr)-k+1):
        a = "".join(strarr[:k])
        if len(a) > len(max_str):
            max_str = a
        del strarr[0]
    return max_str
