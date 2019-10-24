color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new_color = []
for index, item in enumerate(color):
    if index not in (0, 4, 5):
        new_color.append(item)
print(new_color)
