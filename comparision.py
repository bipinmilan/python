list1 = [1, 2, 3, 4]
list3 = [4, 2, 3, 1]
list2 = list1
print(list2)
print(list1)
print(id(list1))
print(id(list2))

# value comparision
print(list1 == list2)

# object comparision
print(list1 is list3)

lst = [1, 2, 3, 4, 5, 6]
lst1 = []
for item in lst:
    if item > 3:
        lst1.append(item)
print(lst1)

list_comprehension_example = [item for item in lst if item > 3]
print(list_comprehension_example)

l = [1, 2, 3, 4, 5]
sum = 0
for item in l:
    sum = sum + item
print(sum)


def last(n): return n[-1]


def sort_list_last(tuples):
    return sorted(tuples, key=last)


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
