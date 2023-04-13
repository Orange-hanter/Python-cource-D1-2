class A(object):
    ...
    
class B(A):
    ...

class C(A):
    ...
    
class D(A):
    ...
    

class E(B,C,D):
    ...
    
class F(D):
    ...
    
class G(E, F):
    ...
    


print(F.mro())
print(E.mro())
print(G.mro())
