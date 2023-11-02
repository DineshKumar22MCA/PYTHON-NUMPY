import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt
"""
eg-match
a-lower bound(default value 0.0)
b-upper bound (default value 1.0)
size
"""

x=random.uniform(size=2)
print(x)
sns.distplot(random.uniform(size=(2)))
plt.show()