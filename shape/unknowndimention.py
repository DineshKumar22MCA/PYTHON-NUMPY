import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y=x.reshape(2,2,-3)
print(y)
a=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
b=a.reshape(-2)
print(b)