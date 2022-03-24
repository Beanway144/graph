import numpy as np

a = np.full((3,4), "=")
a[:,-1] = np.full((3,), "\n")


print(a)
print(a.tobytes().decode('utf-8'))