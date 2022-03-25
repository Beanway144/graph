import numpy as np

# a = np.full((3,4), "=")
# a[:,-1] = np.full((3,), "\n")

a = np.arange(4)
inp = 'y = x + x'
inp = ''.join(inp.split())
print(inp)
l,r = inp.split('=')
# print(a)
print(r.split('x'))