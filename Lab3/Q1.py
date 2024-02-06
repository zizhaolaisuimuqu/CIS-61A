def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """

    '''
def lambda_curry2(func):
    def one(a):
        def two(b):
            return func(a,b)
        return two
    return one
'''

    return lambda x: lambda y: func(x,y)