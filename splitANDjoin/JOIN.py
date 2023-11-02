import numpy as np
a1=np.array([1,2,3])
a2=np.array([4,5,6])
a4=np.array([7,8,9])
a5=np.array([10,11,12])
a3=np.concatenate((a2,a1,a4,a5))
print(a3)

x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
y=np.array([[11,12,13,14,15],[16,17,18,19,20]])
z=np.concatenate((x,y),axis=1)
print(z)