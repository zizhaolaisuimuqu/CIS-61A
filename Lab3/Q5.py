a = lambda x: x * 2 + 1
def b(b, x):
    return b(x + a(x))
x = 3
b(a, x)
