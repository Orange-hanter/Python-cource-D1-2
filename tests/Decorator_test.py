import unittest
from Module6.Decorator import *

def foo():
    return 42

@my_decorator(fun = foo)
class Deco:
    def __init__(self):
        self.x = 107
        
@my_decorator(text = "We come with peace")
class Deco_text:
    def __init__(self):
        self.x = 107

class TestDecorator(unittest.TestCase):
    
    def test_attr_callable(self):
        self.assertEqual(Deco.fun(), foo())
        
    def test_attr_str(self):
        self.assertEqual(Deco_text().text, "We come with peace")
        
        
    def test_wrong_decorator(self):
        with self.assertRaises(TypeError):
            @my_decorator(y = -1)
            class Deco_y:
                ...
    
    def test_warnings(self):
        with self.assertWarns(Warning):
            @my_decorator(zero = lambda x: 0)
            class Deco_y:
                zero = 42