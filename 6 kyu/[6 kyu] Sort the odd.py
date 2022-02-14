def sort_array(source_array):
    odd_num = []
    for i in source_array:
        if i%2!=0: odd_num.append(i)
    odd_num.sort()

    answer = []
    for a in source_array:
        if a%2!=0:
            answer.append(odd_num[0])
            del odd_num[0]
        else: answer.append(a)
    return answer
