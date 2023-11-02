""" guassian filter
loc-mean
scale-standard devition
size-size(array)
"""
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import random
x=random.normal(loc=2,scale=4,size=(1))
print(x)
sns.distplot(random.normal(loc=2,scale=4,size=(1)),hist=True)
plt.show()
