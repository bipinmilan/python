# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y)

z = json.dumps(y)
# the result is a JSON string
print(z)
