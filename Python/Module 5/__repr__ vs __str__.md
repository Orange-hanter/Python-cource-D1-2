
``` python
class X:
     def __repr__(self):
             return "repr"
     def __str__(self):
             return "str"

# intepriter 
x = X()
>>> x
# repr
>>> print(x)
# str
```

Repr часто испльзуется для отладки, для вывода сериализуемого значения полей классов
str выводит читабельное для пользователя представление класса