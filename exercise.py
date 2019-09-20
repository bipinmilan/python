new = []
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for index, item in enumerate(list2):
    new.append([list1[index], item])
print(new)
