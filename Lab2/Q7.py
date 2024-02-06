def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is the sum of the two preceding numbers
    
    >>> fibonacciN(1) 
    1
    >>> fibonacciN(3) 
    2
    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13
    """
    if n < 1 and not isinstance(n,int):
        raise ValueError
    else:
        next_fibonacciN, current_fibonacciN, count = 1, 0, 0
        while count < n:
            next_fibonacciN, current_fibonacciN = current_fibonacciN + next_fibonacciN, next_fibonacciN
            count += 1
        return current_fibonacciN