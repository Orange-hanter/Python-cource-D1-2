my_list = [1,2,3]

G_iterator = iter(my_list)

for x in G_iterator:
    print(x)

#try:
#    while True:
#        x = next(iterator)
#except StopIteration:
#    pass
#
#print(list(enumerate(my_list)))


class MyEnumerate:
    class Iterator:
        def __init__(self, iterator ) -> None:
            self.iterator = iterator
            self.position = -1
        
        def __iter__(self):
            return self
        
        def __next__(self):
            self.position += 1
            return self.position, next(self.iterator)
        
    def __init__(self, iterable) -> None:
        self.iterable = iterable
    
    def __iter__(self):
        return MyEnumerate.Iterator(iter(self.iterable))
    
    

def MyGenEnumerate(iterator):
    position = -1
    for item in iterator:
        position += 1
        yield position, item
    
    
    
    
print(list(MyGenEnumerate(my_list[::-1])))

#print(list(MyEnumerate(my_list[::-1])))

#dictionary = {str(x) : x for x in range(10)}
#print (type(dictionary))
#print (dictionary)
#
#print(list(enumerate(dictionary)))
#print(list(MyEnumerate(dictionary)))
#
##for e in My_enumerate(my_list[::-1]):
##    print(e)
#
#def my_generator():
#    try:
#        while True:
#            x = yield 42
#    except Exception:
#        print(x)
#        
#        
#print(type(my_generator))
#
#