import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(x)
a=x.reshape(4,3)
print(a)
b=x.reshape(2,3,2)
print(b)
c=x.reshape(2,3,2).base
print(c)
