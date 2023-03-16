# Write a simple program which counts the maximum number of occurrences of one byte in a row in given file.
# For example, processing bytes b"aabbbaaaacc" (taken from file arg) returns ("a", 4) as result.

import itertools
from functools import reduce


def my_generator():
    try:
        while True:
            x = yield 42
    except Exception:
        print(x)


g = my_generator()

for i in range(0, 10):
    print(next(g))
    g.send(12)
    try:
        if (i > 3):
            g.throw(Exception(""))
    except StopIteration:
        break


counter = itertools.count()
data = [100, 200, 300, 400]
ordered_data = list(zip(counter, data))
ordered_data2 = list(itertools.zip_longest(range(10), data))
print(ordered_data)
print(ordered_data2)

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

squares = itertools.starmap(pow, [(x, 2) for x in range(3)])
print(list(squares))


def my_odd(n):
    if n % 2:
        return True
    return False


numbers = filter(my_odd, [1, 2, 3, 4, 5, 6])
print(list(numbers))

numbers = itertools.filterfalse(my_odd, [1, 2, 3, 4, 5, 6])
print(list(numbers))

reduce_res = reduce(lambda x, y: x*y, [1, 2, 3])
print(reduce_res)

r = 0
for i in range(100):
    r += i

print(r)

seqTuple = ('g', 'e', 'e', 'k', 's')
print(seqTuple)
print(list(reversed(seqTuple)))

seqRange = range(1, 5)
print(reversed(seqRange))
print(list(reversed(seqRange)))

print(sorted("This is a test string from Andrew".split(), key=str.lower))

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