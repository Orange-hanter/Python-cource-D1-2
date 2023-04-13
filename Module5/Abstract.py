from abc import ABC, abstractmethod


class A(ABC):
    
    @abstractmethod
    def inherited(self):
        pass
    
    
    
class B(A):
    def inherited(self):
        print("reimplemented")
        
        
b = B()
b.inherited()

#a = A()

print(B.__mro__)