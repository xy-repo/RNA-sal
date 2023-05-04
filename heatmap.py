import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
import numpy as np 

df = pd.read_csv('sum_gene.csv',index_col=0)
df = np.log10(df) 
df = df[:50]
df.columns = ['log10(CPM)']
print(df)
plt.figure(figsize=(6,10))
sns.heatmap(df)
#plt.xlabel('log10(CPM)')
plt.tight_layout()
plt.savefig('heatmap.png')