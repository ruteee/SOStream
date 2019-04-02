from utils import min_dist, dist
from find_neighbors import find_neighbors
from update_cluster import updateCluster
from find_overlap import find_overlap
from merge_clusters import merge_clusters
from new_cluster import newCluster


class SOStream:

    def __init__(self, alpha = 0.1, min_pts = 10):
        self.alpha = alpha
        self.min_pts = min_pts
        self.M = list()

    def process(self, vt):
        winner_micro_cluster = min_dist(vt, self.M[-1])
        if len(self.M[-1]) >= self.min_pts:
            winner_neighborhood = find_neighbors(winner_micro_cluster, self.min_pts, self.M[-1])
            if dist(vt, winner_micro_cluster['C'] < winner_micro_cluster['r']):
                updateCluster(winner_micro_cluster, vt, self.alpha, winner_neighborhood)
            else:
                newCluster(self.M, vt)
            overlap = find_overlap(winner_micro_cluster, winner_neighborhood)
            if len(overlap) > 0:
                merge_clusters(winner_micro_cluster, overlap)
        else:
            newCluster(self.M, vt)

    pass