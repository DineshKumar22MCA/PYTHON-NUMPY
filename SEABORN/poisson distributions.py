import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt
"""
lam-rate of occurance
size
"""
x=random.poisson(lam=2,size=(5))
print(x)
sns.distplot(random.poisson(lam=2,size=(5)))
plt.show()