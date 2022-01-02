def find_even_index(arr):
    for idx, num in enumerate(arr):
        if sum(arr[:idx]) == sum(arr[idx+1:]):
            return idx
    return -1
