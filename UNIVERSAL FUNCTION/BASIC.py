x=[1,2,3,4,5]
y=[6,7,8,9,10]
z=[]
for i,j in zip(x,y):
    z.append(i+j)
print(z)

import numpy as np
a=np.add(x,y)
print(a)

def fun(x,y):
    return x+y
fun1=np.frompyfunc(fun,2,1)
print(fun1([1,2,3],[4,5,6]))