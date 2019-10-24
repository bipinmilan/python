l1 = [1, 2]
l2 = [4, 5]
l3 = []
for index, item in enumerate(l1):
    l3.append([l1[0], l2[index]])
for index, item in enumerate(l2):
    l3.append([l1[1], l2[index]])
print(l3)
