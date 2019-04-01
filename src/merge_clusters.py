from utils import dist, weighted_mean

merge_threshold = 0 # Corrigir

def merge_clusters(win_micro_cluster, overlaping_micro_clusters):
    for micro_cluster in overlaping_micro_clusters:
        if dist(micro_cluster, win_micro_cluster) < merge_threshold:
            merge(micro_cluster, win_micro_cluster)
    pass


def merge(cluster_a, cluster_b):
    new_cluster_centroid = [weighted_mean(a, b, cluster_a['n'], cluster_b['n']) for a, b in zip(cluster_a['C'], cluster_b['C'])]
    new_cluster_radius = dist(cluster_a['C'], cluster_b['C']) + max(cluster_a['r'], cluster_b['r'])
    new_cluster = {'n': cluster_a['C'] + cluster_b['C'], 'r': new_cluster_radius, 'C':new_cluster_centroid}
    pass
