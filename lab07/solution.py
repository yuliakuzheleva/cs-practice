import numpy as np
def reshape_rows(values, width):
    if width <= 0 and len(values) % width != 0:
        return[]
    a = np.asarray(values).reshape(-1, width)
    return a.tolist()
def column_means(matrix):
    if not matrix:
        return[]
    a = np.asarray(values).mean(axis=0)
    return np.round(means, 6).tolist()
