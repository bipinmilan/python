# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User1:
    def func1(self):
        print("I'm User1")


class User3:
    def func1(self):
        print("I'm User3")

    def func3(self):
        print("I'm fun3")


class User2(User1, User3):
    def __init__(self):
        pass


b = User2()
print(b.func1())
print(b.func3())
