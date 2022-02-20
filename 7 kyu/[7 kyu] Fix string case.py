def solve(s):
    a = 0
    for i in s:
        if i == i.lower(): a+=1
    return s.lower() if a>=len(s)//2 else s.upper()
