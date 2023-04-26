
List comprehentions

```python
# my_list = [x-expresion for x-object in iterable-generator]
my_list = [x for x in range(0,10)]
```


Dict comprehentions
```python
my_dict = {key:key+1 for key in range(0,10) if key%2==0} #{0: 1, 2: 3, 4: 5, 6: 7, 8: 9}
```


set comprehentions
```python
my_set = {value%5 for value in range(0,10)} # {0, 1, 2, 3, 4}
```

<hr>

Generator comprehentions
PEP 289
```python
g = (n**2 for n in (1, 2, 3))
g.next()
g.close()
```


Generator
```python
def my_generator():
    try:
            while True:
                    x = yield 42
    except Exception:
            print(x)


g = my_generator()
for i in range(0,10):
    print(next(g))
    g.send(12)
    try:
        if (i > 3):
            g.throw(Exception(""))
    except StopIteration:
        break
```


```python
def chain(*iterables): 
	for it in iterables: 
		yield from it 
		
g = chain([1, 2, 3], {'A', 'B', 'C'}, '...') 
print(list(g)) # [1, 2, 3, 'A', 'B', 'C', '.', '.', '.']
```

Iterable
```python
    class Test:

	def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 10
        return self

    def __next__(self):
        x = self.x
        if x > self.limit:
            raise StopIteration
        self.x = x + 1;
        return x


for i in Test(15):
	print(i)
```