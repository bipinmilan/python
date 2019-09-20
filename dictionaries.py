# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
person = {
    'name': 'hari',
    'address': 'dang'
}

print(person['name'])
person['phone'] = 123
print(person)

person.pop('phone')
print(person)

print(person.keys()) #to print all the keys in dictionary
print(person.values()) #to print all the values in dictionary

