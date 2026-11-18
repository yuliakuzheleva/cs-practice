import numpy as np 
def make_hours():
    return np.arange(0, 24, 3).tolist()
def vector_report(values):
    a = np.asarray(values, dtype = float)
    return {"third": a[2], 
            "last": a[-1], 
            "middle": a[2:6].tolist(), 
            "every_second": a[::2].tolist(), 
             "reversed": a[::-1].tolist()}
def change_vector(values):
    a = np.asarray.copy()
    a[2:5] = 99
    a[::2] = -1
    return a.tolist()
def cap_above(values, limit):
    a = np.asarray(values, dtype = float).copy()
    a[a > limit]=limit
    return a.tolist()
def celsius_to_fahrenheit(values):
    a = np.asarray(values, dtype = float)
    fahrenheit = a * 9 / 5 + 32
    return fahrenheit.tolist()


