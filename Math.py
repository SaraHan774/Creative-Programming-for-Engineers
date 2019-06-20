def square(x):
    return x * x


def sqrt(x):
    return x ** 0.5


def distance(p1, p2):
    return sqrt(square(p1['x'] - p2['x']) + square(p1['y'] - p2['y']))

