from math import exp
from utils import dist


def updateCluster(win_micro_cluster, vt, alpha, winner_neighborhood):
    win_micro_cluster.centroid = (win_micro_cluster.number_points * win_micro_cluster.centroid + vt) / (win_micro_cluster.number_points+1)
    win_micro_cluster.number_points += 1
    width_neighbor = win_micro_cluster.radius ** 2
    for neighbor_micro_cluster in winner_neighborhood:
        influence = exp(-(dist(neighbor_micro_cluster.centroid, win_micro_cluster.centroid)/(2 * width_neighbor)))
        neighbor_micro_cluster.centroid = neighbor_micro_cluster.centroid + alpha*influence*(win_micro_cluster.centroid-neighbor_micro_cluster.centroid)
