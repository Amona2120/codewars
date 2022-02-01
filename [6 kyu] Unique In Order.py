def unique_in_order(iterable):
    if len(iterable) == 0: return []
    if len(iterable) < 2: return [iterable]
    if len(iterable) == 2: return [iterable[0]]
    return [iterable[i] for i in range(len(iterable)) if iterable[i] !=iterable[i-1]]
