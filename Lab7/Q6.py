def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    x, y, count = 0, 1, 1
    def helper():
        nonlocal x, y, count
        if count:
            count = 0
            return 0
        else:
            x, y = y, y + x
            return x
    return helper