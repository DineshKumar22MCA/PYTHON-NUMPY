from numpy import random

x = random.choice([1, 2, 3, 4, 5, 6],p=[0.1,0.2,0.2,0.3,0.1,0.1],size=(1))
print(x)
x = random.choice([1, 2, 3, 4, 5, 6],p=[0.1,0.2,0.2,0.3,0.1,0.1],size=(2,2))
print(x)

