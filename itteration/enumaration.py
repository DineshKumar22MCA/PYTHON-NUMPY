import numpy as np

a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
for i in np.ndenumerate(a):
    print(i)

for idx,i in np.ndenumerate(a):
    print(idx,i)
