from tree import *

def height(t): 
    """Return the height of a tree. 
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)]) 
    >>> height(t) 
    2
    """
    if is_leaf(t):
        return 0
    return 1 + max(height(branch) for branch in branches(t))