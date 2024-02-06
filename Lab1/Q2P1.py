#Q2P1
from math import pi

def sphere_area(r):
    """ Area of a sphere with radius r.
    >>> sphere_area(1)
    12.566370614359172
    """
    return 4 * pi * r**2


def sphere_volume(r):
    """ Volume of a sphere with radius r.
    >>> sphere_volume(1)
    4.1887902047863905
    """
    return 4 / 3 * pi * r**3
