from math import sqrt
from data import *
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    x1 = get_lat(city1)
    y1 = get_lon(city1)
    x2 = get_lat(city2)
    y2 = get_lon(city2)
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)