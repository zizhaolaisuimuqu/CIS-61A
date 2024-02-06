def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.
    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if len(str(n)) == 1:
        return 0
    else:
        return ten_pairs(n // 10) + helper(n // 10, n % 10)     #check if every last digit is match the every single dight except himself


def helper(n,m):
    """
    n is the digit of the number except the last digit
    m is the last digit of number
    """
    if n == 0:
        return 0
    elif n % 10 + m == 10:
        return 1 + helper(n // 10, m)
    else:
        return helper(n // 10, m)