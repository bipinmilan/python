new = []
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for index, item in enumerate(list1):
    new.append([item, list2[index]])
print(new)
