def fadingAll(M, t_current, var_lambda, fadeThreshold):
  M_copy = M.copy()
  for microcluster in M_copy:
    t = t_current - microcluster['t']
    fading = microcluster.number_points*2**(-var_lambda*t)
    if fading < fadeThreshold:
      M.remove(microcluster)