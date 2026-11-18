import numpy as np 
def make_hours():
    return np.arange(0, 24, 3).tolist()
def vector_report(values):
    a = np.asarray(values, dtype = float)
    return {"third": a[2], 
            "last": a[-1], 
            "middle": a[2:6], 
            "every_second": a[::2], 
             "reversed": a[::-1]}


