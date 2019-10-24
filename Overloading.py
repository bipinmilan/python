class A:
    def fun1(self, a, b):
        print(a + b)


class B:
    def fun1(self, a, b, c):
        print(a + b + c)


b = B()
#b.fun1(2, 3)
b.fun1(2, 3, 5)
