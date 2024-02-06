'''Memery Killer: Recursive'''

def make_keeper(n): 
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n  where calling cond(i) returns True.
 
    >>> def is_even(x):
    ... #Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def cond(funcs):
        if n > 0:
            make_keeper(n - 1)(funcs)
            if funcs(n):
                print(n)
    return cond