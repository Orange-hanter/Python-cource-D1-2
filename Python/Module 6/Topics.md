- exceptions: usage, blocks, standard exceptions, handling exceptions, re-raising exceptions, raise from  
- context managers, protocol and magic methods, be ready to write, @contextlib how to use it to write ctx manager  
- decorators: usage, decorators with args, nested decorators, functools std module (partial, wraps, update_wrapper)  
- modules and packages: usage, how import works step by step(!) 3-4 steps, packages usage, relative imports, from ... as keywords

 Task:
 Write a dummy class decorator with keyword args (**kwargs).   
 For each of key in kwargs get value (kwargs[key]):  if value is function create respective staticmethod in the decorated class with key name.   
 For each string value, create respective class attribute (cls.key = kwargs[key]).   
 For all other value types raise an Error.   
 If the class already has a reachable attribute with such name, do not add attribute, but print a warning with module 'warnings'
