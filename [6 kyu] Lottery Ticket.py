def bingo(ticket,win):
    results = []
    for key, value in ticket:
        for i in key:
            if ord(i) == value:
                results.append(1)
                break
    return 'Winner!' if results.count(1) >= win else 'Loser!'
