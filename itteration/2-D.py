import numpy as np
a=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in a:
    print(i)
print(' ')
for i in a:
    for j in i:
        print(j)