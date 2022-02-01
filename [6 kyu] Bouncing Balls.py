def bouncing_ball(h, bounce, window):
    if h<1 or 0 > bounce or bounce >= 1 or window >= h: return -1
    ball = h * bounce
    counter = 1
    if window == ball: return counter
    while window <= ball:
        ball *= bounce
        round(ball, 2)
        counter += 2
    return counter
