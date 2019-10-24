# A function is a block of code which only runs when it is called.
# In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces



# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions

def func1():
    a = 20

    def func2():
        nonlocal a #we are modifying value of a so use nonlocal
        a = a + 1
    func2()
    return a


print(func1())


