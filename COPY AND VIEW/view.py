import numpy
a=numpy.array([1,2,3,4,5])
print(a)
y=a.view()
print(y)
a[0]=10
print(a)
print(y)