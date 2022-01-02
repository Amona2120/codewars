def find_it(seq):
    counter = 0
    for i in seq:
        curr_frequency = seq.count(i)
        if curr_frequency % 2 != 0:
            return i
