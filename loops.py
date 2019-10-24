# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


# While loops execute a set of statements as long as a condition is true.
list1 = ['a', 'b', 'c', 'd']

# when we need only item from the list
for item in list1:
    print(item)

# when we need only index from the list
for index in range(len(list1)):
    print(index)

# when we need both index & item from the list
for index, item in enumerate(list1):
    print(index, item)

