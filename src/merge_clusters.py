from utils import dist

merge_threshold = 0 # Corrigir

def merge_clusters(win_micro_cluster, overlaping_micro_clusters):
    for micro_cluster in overlaping_micro_clusters:
        if dist(micro_cluster, win_micro_cluster) < merge_threshold:
            merge(micro_cluster, win_micro_cluster)


def merge(cluster_a, cluster_b):

    pass