def SunnyRate(SunnyDays,TotalDays):
    """
    >>> SunnyRate(15,30)
    50%
    >>> SunnyRate(10,30)
    33%
    >>> SunnyRate(20,30)
    66%
    """
    print("{}%".format(int((SunnyDays / TotalDays) * 100)))