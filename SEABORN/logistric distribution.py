import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt
"""
loc-mean(0.0)
scale-standard devition
size
"""
x=random.logistic(loc=1,scale=2,size=(2))
print(x)
sns.distplot(random.logistic(loc=1,scale=2,size=(2)))
plt.show()