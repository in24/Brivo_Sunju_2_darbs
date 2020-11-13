import math


def vienadojums(a, b, c):
    d = b*b-4*a*c
    if d > 0:
        x1 = (-b+math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        return [x1, x2]
    elif d == 0:
        x = -b/(2*a)
        return [x]
    else:
        return None


print(vienadojums(5, 16, 3))
