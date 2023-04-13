from abc import ABC


class A:
    #def __new__(cls):
    #    print(cls)
    #    return None
    xyz = 43
    
    def method(self):
        print(self)
        
    def __init__(self):
        #print(A.__mro__)
        #print("init")
        print(self.xyz)
        print(A.xyz)
        #arg[0].x = 42
    

    #def __radd__(): ?
    
    def __call__():
        ...
    
    
    def gg(self):
        ...
        
    
#print(type(type(A)))
#print(A())

a = A()
a.xyz = 42
del a.xyz
print(a.xyz)
print(A.__dict__)
A.method(a)