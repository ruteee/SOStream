def newCluster(M, vt):
    new_cluster = {'n': 1, 'r': 0, 'C':vt}
    new_mt = M[-1].copy()
    new_mt.append(new_cluster)
    M.append(new_mt)