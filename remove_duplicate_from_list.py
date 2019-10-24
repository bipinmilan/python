list1 = ['bipin', 'basnet', 'milan', 'dang', 'bi', 'mi', 'pi', 'b']
list2 = []
n = int(input("enter n:"))
for word in list1:
    if len(word) > n:
        list2.append(word)
print(list2)


# remove duplicate item from list
def remove_duplicate_from_list(mylist):
    # create a dictionary where keys are list items, dictionary automatically remove duplicate items
    # finally convert dictionary back into list
    return list(dict.fromkeys(mylist))


print(remove_duplicate_from_list([10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]))

# or next method without function
my_list = ['bipin', 'milan', 'bipi', 'milan', 'hero', 'zero', 'zero']
my_list = list(dict.fromkeys(my_list))
print(my_list)

# check if list is empty or not
empty = [1, 2]
if len(empty) == 0:
    print("list is empty")
else:
    print("list is not empty")
