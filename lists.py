# A List is a collection which is ordered and changeable. Allows duplicate members.
list1 = [1, 2, 3]
list2 = list1
print(id(list1))
print(id(list2))

l1 = [1, 2, 3]
l2 = l1
l1.append(5)
print(l1)
print(l2)
print(id(l1))
print(id(l2))

list4 = [1, 3, 4, 5]
list4.append(6)
list4.pop(3)
print(list4)

lt = ["hello", "world", 1, 2, 3, 4, 5]
lt.pop(2)
lt.remove("hello")
lt.remove(5)
print(lt)

