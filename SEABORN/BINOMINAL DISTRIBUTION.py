import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
"""
eg-coins spin
n-num of trial
p-probability
size
"""
x=random.binomial(n=10,p=0.5,size=5)
print(x)
sns.distplot(random.binomial(n=10,p=0.5,size=5),hist=True)
plt.show()
