"""
Write a class which creates obj. Class must implement:
a) __getattribute__ checks if attr name  == "hello" -> return "hello world" else -> default behavior 
b) __getattr__ checks if attr name  == "love" -> return "love you" else -> return None 
c) __setattr__ checks if attr name  == "vasia" -> assign obj.name = "pupkin" else -> assign obj.name = value 
d) write test to prove if everything works 
"""


class Uber:
    def __init__(self):
        self._atr = 42
        self.__atr2 = 43

    def __getattribute__(self, name):
        print("__getattribute__", name)
        if name == "hello":
            return "Hello world"
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        print("__setattr__", name, value)
        if name == "vasia":
        #    return object.__setattr__(self, name + "pupkin", value)
            self.vasiapupkin = value
        return super().__setattr__(name, value)
    
    def __getattr__(self, name): 
        print("__getattr__", name)
        if name == "love":
            return "love you"
        #return object.__getattr__(self, value)
        return None


u = Uber()
u.gg = 107
u.vasia = 12
print(u._Uber__atr2)
print(u.__dict__)
print(u.uao)
