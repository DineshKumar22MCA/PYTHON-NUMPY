import numpy as np
a=np.array([41,42,43,44,45])
y=np.array([True,False,True,False,True])
x=a[y]
print(x)

f=[]
for i in a:
    if i >=42:
        f.append(True)
    else:
        f.append(False)
print(f)
s=a[f]
print(s)
