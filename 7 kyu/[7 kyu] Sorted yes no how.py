def is_sorted_and_how(arr):
    if arr == sorted(arr): return "yes, ascending"
    if arr == sorted(arr)[::-1]: return "yes, descending"
    return "no"
