def f(its):
    res = []
    for x in "abcde":
        def foo(x):
            return lambda: its * x
        res.append(foo(x))
    return res


# ------------------- NOT CHANGEBLE ! 
print( [x() for x in f(2) ])
print( [x() for x in f(3) ])
print( [x() for x in f(4) ])