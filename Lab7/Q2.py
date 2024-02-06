def group_by(seq, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    d = {}
    for i in seq:
        if d.get(fn(i)):
            d[fn(i)].append(i)
        else:
            d[fn(i)] = [i]
    return dict(sorted(d.items()))