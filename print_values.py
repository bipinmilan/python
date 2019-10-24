# generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included)


my_list = []
for i in range(1, 31):
    my_list.append(i ** 2)
print(my_list[:5])
print(my_list[-5:])
