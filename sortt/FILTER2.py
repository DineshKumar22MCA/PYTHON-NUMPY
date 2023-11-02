import numpy as np
a=np.array([10,20,35,40,50])
f=a>25
b=a[f]
print(b)

f1=a%2!=0
c=a[f1]
print(c)