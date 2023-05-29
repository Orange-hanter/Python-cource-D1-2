дикт нельзя хешировать, ключи это и есть хеши

### [hashable](https://docs.python.org/3.11/glossary.html#term-hashable "Permalink to this term")

An object is _hashable_ if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash value.

Hashability makes an object usable as a dictionary key and a set member, because these data structures use the hash value internally.

Most of Python’s immutable built-in objects are hashable; mutable containers (such as lists or dictionaries) are not; immutable containers (such as tuples and frozensets) are only hashable if their elements are hashable. Objects which are instances of user-defined classes are hashable by default. They all compare unequal (except with themselves), and their hash value is derived from their [`id()`](https://docs.python.org/3.11/library/functions.html#id "id").