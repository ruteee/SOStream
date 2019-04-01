from math import sqrt

def dist(v1, v2):
    dist = [(a - b)**2 for a, b in zip(v1, v2)]
    dist = sqrt(sum(dist))
    return dist