from math import sqrt

def dist(v1, v2):
    dist = [(a - b)**2 for a, b in zip(v1, v2)]
    dist = sqrt(sum(dist))
    return dist


def weighted_mean(a, b, mean_a, mean_b):
    return ((mean_a * a + mean_b * b)/(mean_a + mean_b))


def min_dist(vt, micro_clusters):
    micro_cluster_min_dist = float('inf')
    min_micro_cluster = None
    for micro_cluster in micro_clusters:
        dist_to_micro_cluster = dist(vt, micro_cluster['C'])
        if dist_to_micro_cluster <= micro_cluster_min_dist:
            micro_cluster_min_dist = dist_to_micro_cluster
            min_micro_cluster = micro_cluster
    
    return min_micro_cluster
