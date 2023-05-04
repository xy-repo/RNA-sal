import pandas as pd 
import mygene
from tqdm import tqdm 


mg = mygene.MyGeneInfo()

df = pd.read_csv('out_prefixReadsPerGene.out.tab',sep='\t',index_col=0)
df = df.iloc[3:,1]
df = df[df!=0]
sum_num = df.sum()
df = (df/sum_num)*1e6
df = df.sort_values(ascending=False)
df.index = [x.split('.')[0] for x in df.index]
df = df[:1000]

gene_lst = []
for g in tqdm(df.index):
    try:
        name = mg.getgene(g, fields='symbol')['symbol']
    except:
        name = g
    gene_lst.append(name)

df.index = gene_lst

print(df)
df.to_csv('sum_gene.csv')
