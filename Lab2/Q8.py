def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    if n <= 1 or not(isinstance(n,int)):
            return False
    else:
        i = n
        while i > 2:
           i -= 1
           if n % i == 0:
                return False
    return True