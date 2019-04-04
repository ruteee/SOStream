import numpy as np
import pandas as pd
import utils

def find_neighbors(win_microcluster, min_pts, model_t):
  if len(model_t) >= min_pts:
    win_dist = []
    for microcluster in model_t:
      win_dist.append(utils.dist(microcluster.centroid, win_microcluster.centroid))
    win_dist.sort()
    idx_microclusters = np.argsort(win_dist)
    
    k_dist = win_dist[min_pts-1]
    win_microcluster.radius = k_dist
    win_nn = [model_t[idx] for idx in idx_microclusters[0:(min_pts)]]
    return win_nn
  else:
    return []

