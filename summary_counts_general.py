#!/usr/bin/python
import pandas as pd
import os

def get_data():
    df_sum = pd.DataFrame()
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            filename = filename.lower()
            if filename.endswith('.csv'):
                df = pd.read_csv(filename, skiprows=1, header=0, names = ['genes', filename+'_counts'])
                #print df
                df_indexed = df.set_index(df['genes'])
                del df_indexed['genes']
                #print df_indexed
                df_sum = pd.concat([df_sum, df_indexed], axis=1)
        df_sum.to_csv('compiled_gene_counts.txt', na_rep = 'NA' )
        print df_sum
get_data()
