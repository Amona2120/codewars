def diamond(n):
    if n%2==0 or n<1: return None

    answer = ""
    spaces = n//2
    times = 1
    for i in range(n//2+1):
        answer += " "*(spaces)+"*"*times+"\n"
        spaces -= 1
        times +=2

    spaces += 2
    times -= 4
    for i in range(n//2):
        answer += " "*(spaces)+"*"*times+"\n"
        spaces += 1
        times -=2
    return answer
