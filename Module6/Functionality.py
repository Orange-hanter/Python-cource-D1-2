"""
Write the python code with the following requirements to be met:
>  (a) write function which return sum of 2 int arguments, annotate args, write function docstring
>  (b) write 'double decorator', which returns function which doubles the return value of input_function
>  c) write wraps2 function the similar as functools.wraps, with the following diffs:  
>   1) only match __annotations__, and __docs__ and no other attributes;
>   2) in wraps2, perform additional logging print to stdout indicating wrapped function name and it's id
>  d) rewrite (b) applying (c), so that decoration of function (a) with (b) preserves  
>      original attributes described in (c), test results
"""
import functools


# Patr A and B

def doubler(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return wrapper


@doubler
def my_sum(a: int, b: int):
    """
    Regular function for student research purpose.
    """
    return a + b


# Part C
def wraps2(src_fnc):
    print("wraps2-->", id(src_fnc), src_fnc.__name__)
    return functools.wraps(wrapped=src_fnc, assigned=("__doc__", "__annotations__"))


def doubler2(func):
    @wraps2(func)
    def wrapper(*args):
        return func(*args) * 2

    return wrapper


@doubler2
def my_sum2(a: int, b: int) -> int:
    """
    Regular function for student research purpose.
    """
    return a + b


# TEST

print('=' * 10, "Clear decorator", '=' * 10)
help(my_sum)
print('=' * 10, "Decorator with custom wraps", '=' * 10)
help(my_sum2)
