# Enclosed case
def sum(digit=None):
    acm = digit

    def wrapped(sub=None):
        if sub:
            return sum(acm + sub)
        else:
            return acm

    if not digit == None:
        return wrapped
    else:
        return 0


# Nonlocal case
def sumV2(digit=None):
    acm = digit

    def wrapped(sub=None):
        nonlocal acm
        if sub:
            acm += sub
            return wrapped
        else:
            return acm

    if not digit == None:
        return wrapped
    else:
        return 0


# Global case
acm = 0


def sum2(digit=None):
    global acm
    if digit:
        acm += digit
        return sum2
    else:
        result, acm = acm, 0
        return result


# Attributes case
def sum3(digit=None):
    if digit:
        sum3.static_var += digit
        return sum3
    else:
        result, sum3.static_var = sum3.static_var, 0
        return result


sum3.static_var = 0


# Test case
if __name__ == "__main__":
    for name, f in {"Enclosed": sum, "Nonlocal": sumV2, "Global": sum2, "Attributes": sum3}.items():
        print(f"{name} run:")
        print("res:", f())
        print("res:", f(1)())
        print("res:", f(1)(2)())
        print("res:", f(1)(2)(3)())
        print("res:", f(1)(2)(3)(4)(5)())
