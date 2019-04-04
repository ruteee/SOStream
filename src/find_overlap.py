import pandas as pd
import utils

def find_overlap(win, win_nn):
  overlap = []
  for microcluster in win_nn:
    if win is not microcluster:
      if utils.dist(win.centroid, microcluster.centroid) - (win.radius + microcluster.radius) < 0 :
        overlap.append(microcluster)
  return overlap
