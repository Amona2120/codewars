def find_uniq(arr):
    set_arr = set(arr)
    for i in set_arr:
        if arr.count(i) == 1:
            return i
