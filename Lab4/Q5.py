def gcd(a, b):
    """ Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if max(a,b) % min(a,b) == 0:
        return b
    else:
        return gcd(min(a,b),max(a,b) % min(a,b))