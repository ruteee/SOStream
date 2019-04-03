from utils import dist, weighted_mean


def merge_clusters(win_micro_cluster, overlaping_micro_clusters, merge_threshold):
    merged_cluster =  win_micro_cluster.copy()
    deleted_clusters = list()
    for micro_cluster in overlaping_micro_clusters:
        if dist(micro_cluster['C'], win_micro_cluster['C']) < merge_threshold:
            merged_cluster = merge(micro_cluster, merged_cluster)
            if len(deleted_clusters) == 0:
                deleted_clusters.append(win_micro_cluster)
            deleted_clusters.append(micro_cluster)
    return merged_cluster, deleted_clusters


def merge(cluster_a, cluster_b):
    new_cluster_centroid = [weighted_mean(a, b, cluster_a['n'], cluster_b['n']) for a, b in zip(cluster_a['C'], cluster_b['C'])]
    new_cluster_radius = dist(cluster_a['C'], cluster_b['C']) + max(cluster_a['r'], cluster_b['r'])
    new_cluster = {'n': cluster_a['n'] + cluster_b['n'], 'r': new_cluster_radius, 'C':new_cluster_centroid}
    return new_cluster
