l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']
l3 = []
print(len(l1))
for index, item in enumerate(l1):
    if index == len(l1)-1:
        l3.append([l1[index], l2[0]])
    else:
        l3.append([l1[index], l2[index+1]])
print(l3)


