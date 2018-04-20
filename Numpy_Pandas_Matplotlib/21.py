import matplotlib.pyplot as plt
import matplotlib
import csv
import numpy as np
import pandas as pd
f =  pd.read_csv('CGHS_dispensary_list_1.csv')
#c_data = f["category"]
a=len(f[f.category=="alopathic"])
b=len(f[f.category=="homeo"])
c=len(f[f.category=="siddha"])
d=len(f[f.category=="unani"])
e=len(f[f.category=="ayurvedic"])
labels = 'alopathic', 'homeo', 'siddha', 'unani', 'ayurvedic'
a1 = [a,b,c,d,e]

plt.pie(a1, labels=labels)
plt.axis('equal') 
plt.show()
