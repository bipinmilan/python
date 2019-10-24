def match_string(words):
    ctr = 0
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr = ctr + 1
    return ctr


print(match_string(['343', 'non', 'aba', '454545']))

# or next method

words = ['242', 'aa', 'mom', 'xyz', 'aaa', '5566445']
c = 0
for word in words:
    if len(word) > 2 and word[0] == word[-1]:
        c = c + 1
print(c)
