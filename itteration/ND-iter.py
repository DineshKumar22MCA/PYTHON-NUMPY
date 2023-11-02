import numpy as np

a = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]])
for i in np.nditer(a):
    print(i)

b=np.array([1,2,3,4,5])
for i in np.nditer(a,flags=["buffered"],op_dtypes=["S"]):
    print(i)

x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
for i in np.nditer(x[:,::2]):
    print(i)


