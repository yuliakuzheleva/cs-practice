import numpy as np
def reshape_rows(values, width):
    if width <= 0 or len(values) % width != 0:
        return[]
    a = np.asarray(values).reshape(-1, width)
    return a.tolist()
def block(matrix, rows, columns):
    if not matrix:
        return []
    a = np.asarray(matrix, dtype=float)
    selected = a[np.ix_(rows, columns)]
    return selected.tolist()
def column_means(matrix):
    if not matrix:
        return[]
    a = np.asarray(matrix).mean(axis=0)
    return np.round(a, 6).tolist()
def column_range(matrix, column):
    if not matrix:
        return 0.0
    a = np.asarray(matrix, dtype=float)
    col_data = a[:, column]
    rng = np.ptp(col_data)
    return float(np.round(rng, 6))

