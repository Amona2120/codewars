from itertools import combinations

def choose_best_sum(t, k, ls):
    try:
        return max(sum(i) for i in combinations(ls,k) if sum(i)<=t)
    except:
        return None
