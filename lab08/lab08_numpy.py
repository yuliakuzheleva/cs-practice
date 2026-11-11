import numpy as np
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
unknown_table = np.full((2,3), -1)
identity = np.eye(3)
print(hours)
print(hours.shape)
print(hours.ndim)
print(hours.size)
print(hours.dtype)

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])


