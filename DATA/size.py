import numpy as np
x=np.array([1,2,3,4,5])
print(x.dtype)
x=np.array([1,2,3,4,5],dtype="i4")
print(x.dtype)
y=x.astype("S")
print(y)
print(y.dtype)
z=y.astype(int)
print(z)
print(z.dtype)
x=x.astype(bool)
print(x)
