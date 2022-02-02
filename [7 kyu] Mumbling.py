def accum(s):
    return "-".join((i*(idx+1)).capitalize() for idx, i in enumerate(s))
