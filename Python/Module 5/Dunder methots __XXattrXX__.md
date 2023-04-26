

- `__setattr__(self, key, value)` - call at moment change class feld (operator .)
```python
def __setattr__(self, key, value):
	# forbid setting value for field with key
	return object.__setattr__(self, key, value)
	# return self.__dict__[key] = value
```

- `__getattribute__(self, item)` - call if `item` feeld exist
```python
def __getattribute__(self, item):
	#forbid access for some fields
	return object.__getattribute__(self, item)
```


- `__getattr__(self, item)` - call in case `item` dosn't existh
```python
# now attempt to access not existing field return false insteard exception
def __getattr(self, item):
	return false 
```

- `__delattr__(self, item)` - call in `del` operation call
```python

```

https://docs.python.org/3/reference/datamodel.html?highlight=__getattribute__#object.__getattribute__