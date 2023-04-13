"""
Write a dummy class decorator with keyword args (**kwargs). 
For each of key in kwargs get value (kwargs[key]):  
    - If value is function create respective staticmethod in the decorated class with key name. 
    - For each string value, create respective class attribute (cls.key = kwargs[key]). 
    - For all other value types raise an Error. 
If the class already has a reachable attribute with such name, do not add attribute, but 
print a warning with module 'warnings
"""
import warnings

def my_decorator(**kwargs):
    def wraper(cls:object):
        for key, value in kwargs.items():
            if hasattr(cls, key):
                warnings.warn(f"Attribute {key} already exists and will not be added.")
                continue
            if callable(value): 
                setattr(cls, key, staticmethod(value))
            elif isinstance(value, str): 
                    setattr(cls, key, value)
            else:
                raise TypeError(f"Invalid value type for attribute {key}.")
        return cls  
    return wraper
