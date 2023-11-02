import seaborn as sns
from numpy import random
import matplotlib.pyplot as plt
"""
eg-dice
n-num of posibles out comes
pvals-list of probabilties 
size
we can't use seaborn in this program
"""

x=random.multinomial(n=6,pvals=[1/6,1/6])
print(x)

