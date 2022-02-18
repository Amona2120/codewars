def sum_pairs(lst, s):
    answer = set()
    for i in lst:
        if s - i in answer:
            return [s - i, i]
        answer.add(i)
