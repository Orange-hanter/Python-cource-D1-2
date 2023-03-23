"""
Create class Car with weight attribute (int). 
Car class has 2 methods only: 
    __ init __ (assigns initial value to attribute) 
    and 
    __ add __ 

The last method __ add __ must work only with int arg type, the others returns "TypeError: unsupported operand type(s)" as builtin int does. 
    __add __ return type: int (weight + other:int).

Create similar class Excavator, with only 2 methods __ init__ and __ radd__. 
The __ init __ is the same as above, while __ radd __ must support the following expressions:
    >>> Car(10) + Excavator(20) (return 30 of type int)
At the end, those test must pass:
    >>> Car(10) + 50
    >>> Car(10) + Excavator(20)
Those should raise TypeError:
    >>> Car(10) + 55.55
    >>> 111 + Car(10)
    >>> Excavator(20) + Car(10)
"""


class Car:
    def __init__(self, weight):
        self.weight = weight
    
    def __add__(self, other) -> int:
        print(type(other))
        if not isinstance(other, int): raise TypeError()
        return self.weight + other


class Excavator(int):
    def __init__(self, weight):
        self.weight = weight
    
    def __radd__(self, other):
        if not (type(other) == int or type(other) == Car): raise TypeError()
        return other + self.weight

