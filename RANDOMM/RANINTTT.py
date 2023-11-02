import numpy
from numpy import random
x=random.randint(100)
print(x)
y=random.randint(100,size=(5))
print(y)
y=random.randint(100,size=(5,2))
print(y)
a=numpy.array([1,2,3,4,5,6,7,8,9,10])
print(random.randint(a))