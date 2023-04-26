<hr>
1 "для чего нам нужно LEGB"

Объяснить код
```python
a = 5

def foo():
    print(a)

def foo2():
    if False:
        a = 7
    print(a)
  

foo()
foo2()  
  
print(a)   
foo()   
print(a)
```

Name resolution of free variables occurs at runtime, not at compile time

<hr>

В нескольких вариациях (через атрибуты функции, глобал, нонлокал) написать код который

```python
sum(1)(2)(3)() # returns 6
sum(1)(2)(3)(4)(5)() # returns 15
```

