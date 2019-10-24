d = dict()
for x in range(1, 21):
    d[x] = x ** 2
print(d.keys())


def multiply_list(items):
    tot = 1
    for i in items:
        tot = tot * i
    return tot


print(multiply_list([1, 2, -8]))


