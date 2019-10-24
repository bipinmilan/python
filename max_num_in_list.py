def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(max_num_in_list([2, 9, 3, 0]))



def min_num_in_list(lst):
    min = lst[0]
    for b in lst:
        if b < min:
            min = b
    return min

print(min_num_in_list([-8, 9, 0, 1, 2]))