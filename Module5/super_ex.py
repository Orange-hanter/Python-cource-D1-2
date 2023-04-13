class A(object):
    def foo(self):
        print("A")


class B(A):
    def foo(self):
        print("B")


class C(A):
    def foo(self):
        A.foo(self)
        print("C")
    

class D(B, C):
    def foo(self):
        C.foo(self)
        B.foo(self)
        print("D")


d = D()
d.foo()

print(D.__bases__)
#ACBD