map
```python
squares = map(lambda x: x*x, range(10))
print(list(squares))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = map(lambda x,y: x**y, range(10), itertools.repeat(2))
print(list(squares))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = itertools.starmap(pow, [(x,2) for x in range(3)])
print(list(squares))
# [0, 1, 4]
```


filter
```python
def my_odd(n):
    if n % 2:
        return True
    return False


numbers = filter(my_odd, [1,2,3,4,5,6])
print(list(numbers))
# [1, 3, 5]

numbers = itertools.filterfalse(my_odd, [1,2,3,4,5,6])
print(list(numbers))
# [2, 4, 6]
```


zip
```python
import itertools

counter = itertools.count()
data = [100, 200, 300, 400]
ordered_data = list(zip(counter, data))
ordered_data2 = list(itertools.zip_longest(range(10), data))

print(ordered_data)
# [(0, 100), (1, 200), (2, 300), (3, 400)]
print(ordered_data2)
#[(0, 100), (1, 200), (2, 300), (3, 400), (4, None), (5, None), (6, None), (7, None), (8, None), (9, None)]
```


reduce
```python
# reduse(f, [a,b,c,d]) <--> f(a, f(b, f(c, d) ) )
reduce_res = reduce(lambda x,y: x+y, range(100))
print(reduce_res)
# 4950
```


sorted
```python
print(sorted("This is a test string from Andrew".split(), key=str.lower))
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

print(sorted(student_objects, key=lambda student: student.age))
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```


reversed
```python
seqTuple = ('g', 'e', 'e', 'k', 's')
print(list(reversed(seqTuple)))
# ['s', 'k', 'e', 'e', 'g']

seqRange = range(1, 5)
print(list(reversed(seqRange)))
# [4, 3, 2, 1]
```