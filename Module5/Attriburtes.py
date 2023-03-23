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

    def __getattribute__(self, name):
        if name == "hello":
            return "Hello world"
        return object.__getattribute__(self, name)
    
    def __setattr__(self, name, value):
        if name == "vasia":
            return object.__setattr__(self, name + "pupkin", value)
        return object.__setattr__(self, name, value)
    
    def __getattr__(self, name):
        if name == "love":
            return "love you"
        #return object.__getattr__(self, value)
        return None


u = Uber()
u.gg = 107