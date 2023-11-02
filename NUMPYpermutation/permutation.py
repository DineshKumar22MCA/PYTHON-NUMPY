from numpy import random
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9])
random.permutation(x)
print(x)
y=random.permutation(x)
print(x)
print(y)