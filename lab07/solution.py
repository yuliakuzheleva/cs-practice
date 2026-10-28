import numpy as np
def reshape_rows(values, width):
    if width <= 0 and len(values) % width != 0:
        return[]
    a = np.asarray(values).reshape(-1, width);
    return a
