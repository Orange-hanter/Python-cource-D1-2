#AAA = 41


def bar():
    AAA = 42

    def foo(a):
        print(AAA, a)
    return foo

x = bar()


def clb( fo = bar ):
    ...