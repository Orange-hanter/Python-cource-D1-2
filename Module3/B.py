a = 5


def foo2():
    print(a)
    a = 7

# print(foo)
# print(a)
# foo()
# print(a)


def baz(a, b, c, /, D, E, *, X):
    print(a)
    print(b)
    print(c)
    print(D)
    print(E)
    print(X)


# baz(1, 3, 3, [4,5,6], E=5, X=0)


def foo():
    a = 42
    print(f"foo{a}")

    def bar():
        print(f"bar{a}")

        def baz():
            nonlocal a
            a += 24
            print(f"baz{a}")

            def far():
                print(f"far{a}")
                # a = 0 # UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
            far()
        baz()
    bar()
    print(f"foo{a}")

def quit_game():
    ...

class ob:
    def describe(self):
        print("des")
    def get(self, a,v):
        print(f"get {a}, {v}")
    def neighbor(self, a):
        print(f"ne {a}")
        
current_room = ob()
character = ob()

command = input("What are you doing next? ")
match command.split():
    case ["quit"]:
        print("Goodbye!")
        quit_game()
    case ["look"]:
        current_room.describe()
    case ["get", obj]:
        character.get(obj, current_room)
    case ["go", direction]:
        current_room = current_room.neighbor(direction)
    # The rest of your commands go here
