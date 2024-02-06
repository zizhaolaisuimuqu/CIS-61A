def keep_ints(cond, n):
   """Print out all integers 1..i..n where cond(i) is true

    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
   if n > 0:
      keep_ints(cond, n - 1)
      if cond(n):
         print(n)