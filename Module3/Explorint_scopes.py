# Enclosed case
def sum_enclosed(digit=None):
    acm = digit

    def wrapped(digit=None):
        if digit:
            return sum_enclosed(acm + digit)
        else:
            return acm

    if digit is not None:
        return wrapped
    else:
        return 0


# Nonlocal case
def sum_nonlocal(digit=None):
    acm = digit

    def wrapped(digit=None):
        nonlocal acm
        if digit:
            acm += digit
            return wrapped
        else:
            return acm

    if digit is not None:
        return wrapped
    else:
        return 0


# Global case
acm = 0


def sum_global(digit=None):
    global acm
    if digit is not None:
        acm += digit
        return sum_global
    else:
        result, acm = acm, 0
        return result


# Attributes case
def sum_attributes(digit=None):
    if digit is not None:
        sum_attributes.static_acm += digit
        return sum_attributes
    else:
        result, sum_attributes.static_acm = sum_attributes.static_acm, 0
        return result


sum_attributes.static_acm = 0


# Test case
if __name__ == "__main__":
    for name, f in {"Enclosed": sum_enclosed, "Nonlocal": sum_nonlocal, "Global": sum_global, "Attributes": sum_attributes}.items():
        print(f"{name} run:")
        print("res:", f())
        print("res:", f(0)())
        print("res:", f(1)())
        print("res:", f(1)(2)())
        print("res:", f(1)(2)(3)())
        print("res:", f(1)(2)(3)(4)(5)())
