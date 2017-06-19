#!/bin/python
import pandas as pd

df = pd.read_table('mouse_rRNA_body.text.temp.txt', sep='\t', header=None)
print df.head(3)
df[3]=('rRNA')
print df.head(3)
df.to_csv('mouse_rRNA_list.txt', sep='\t')