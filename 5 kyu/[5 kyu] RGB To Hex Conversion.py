def rgb(r, g, b):
    rgb = _out_of_range(r, g, b)
    return ''.join(_len_four(i) if _what_len(i) else _other_len(i) for i in rgb)


def _out_of_range(r, g, b):
    rgb = [r, g, b]
    for n, i in enumerate(rgb):
        if i > 255:
            rgb[n] = 255
        if i < 1:
            rgb[n] = 0
    return rgb

def _what_len(num):
    return len(hex(num)) == 4

def _len_four(num):
    return str(hex(num)[2:]).upper()

def _other_len(num):
    return str(hex(num)[::2]).upper()
