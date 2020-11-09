import numpy as np
A = np.array(input().split(), float)
x = float(input())
print(np.polyval(A,x))