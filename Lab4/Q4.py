def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def hahaha(divisor):
        if divisor == 1:
            return True
        elif n % divisor == 0:
            return False
        else:
            return hahaha(divisor - 1)
    return hahaha(n - 1)


