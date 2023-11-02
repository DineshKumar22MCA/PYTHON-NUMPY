from numpy import random as rm
x=rm.choice([1,2,3,4,5])
print(x)
x=rm.choice([1,2,3,4,5],size=(3))
print(x)
x=rm.choice([1,2,3,4,5],size=(3,5))
print(x)