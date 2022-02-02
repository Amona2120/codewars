def likes(names):
    length = len(names)
    if names == []:
        return "no one likes this"
    if length == 1:
        return "{} likes this".format(names[0])
    if length == 2:
        return "{} and {} like this".format(names[0], names[1])
    if length == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    return "{}, {} and {} others like this".format(names[0], names[1], length - 2)
