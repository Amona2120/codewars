def what_time_is_it(angle):
    hour = int(angle // 30)
    minute = int((angle % 30) * 2)
    return '{:02d}:{:02d}'.format(hour if hour != 0 else 12, minute)
