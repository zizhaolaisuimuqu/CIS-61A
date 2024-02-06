def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    if n > 1 and isinstance(n,int):
        count = 0
        while n != 1:
            print(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count += 1
        print(1)
        return count +1
    else:
        raise ValueError("Invalid value")