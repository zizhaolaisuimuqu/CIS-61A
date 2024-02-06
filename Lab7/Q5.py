def memory(n): 
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """
    def helper(fn):
        nonlocal n
        n = fn(n)
        return n
    return helper