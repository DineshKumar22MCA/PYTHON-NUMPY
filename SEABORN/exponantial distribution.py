import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt
"""
eg-unexpected increase and decrease
scales-increase (default 1.0)
size
"""
x=random.exponential(scale=2,size=(1))
print(x)
sns.distplot(random.exponential(scale=5,size=(3)),hist=True)
plt.show()

