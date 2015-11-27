from math import sqrt


def solve(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        print("No solutions")
    elif d == 0:
        x = -b / (2*a)
        print("One solution: x = %s" % x)
    elif d > 0:
        x1 = (-b + sqrt(d)) / (2*a)
        x2 = (-b - sqrt(d)) / (2*a)
        print("Two solutions: x1 = %s; x2 = %s" % (x1, x2))
    else:
        print("?????")

solve(1, 1, 1)
solve(1, 2, 1)
solve(1, 5, 6)