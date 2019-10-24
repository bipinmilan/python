# python program to remove even number from list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even = []
without_even = []
for num in my_list:
    if num % 2 == 0:
        even.append(num)
    else:
        without_even.append(num)
print("List after removing even numbers:", without_even)

