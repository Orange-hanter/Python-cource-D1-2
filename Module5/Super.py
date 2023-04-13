class A:
    def foo(self):
        print("A")
        
        
class B(A):
    def foo(self):
        print("B")
        #A.foo(self)
        super().foo()

class C(A):
    def foo(self):
        print("C")
        #A.foo(self)
        super().foo()
        
class D(B, C):
    def foo(self):
        print("D")
        #A.foo(self)
        super().foo()
        

D().foo()
"""
D
B
C   - WHY ?
A
"""