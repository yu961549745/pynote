'''
面向对象编程
'''


class A(object):
    def __init__(self, x):
        self.A = x

    def hello(self):
        pass


class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.B = y

    def __str__(self):
        return 'A=%d,B=%d' % (self.A, self.B)

    def hello(self):
        print("hello")


a = A(1)
b = B(1, 2)
print(b)
b.hello()
a.hello()
