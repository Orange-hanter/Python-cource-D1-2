class MyEnumerate:
    def __init__(self, iterable ) -> None:
        self.iterable = iterable
    
    def __iter__(self):
        position = -1
        for item in self.iterable:
            position += 1
            yield position, item


my_list = [1,2,3]
obj = MyEnumerate(my_list[::-1])

#obj_iterator = iter(obj)
#for i in obj_iterator:
#    print(i)
    
obj_iterator2 = iter(obj)
#for i in obj_iterator2:
#    obj_iterator2.send(42)
#    print(i)
#print(obj_iterator2.send(None))
#print(obj_iterator2.close())
#print(obj_iterator2.send(None))


l = [i*i for i in range(20) if not i % 2]

