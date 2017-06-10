#!/usr/bin/python
import pandas as pd
import unicodecsv
import os

def get_data():
    df_sum = pd.DataFrame()
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            if 'summary_counts' in filename:
                with open(filename, 'rb') as counts_csv:
                    counts_csv.next()
                    reader = unicodecsv.reader(counts_csv)
                    l = list(reader)
                    df = pd.DataFrame(l, columns=['genes', filename+'counts'])
                    df_indexed = df.set_index(df['genes'])
                    del df_indexed['genes']
                    #print df_indexed
                    df_sum = pd.concat([df_sum, df_indexed], axis=1)
    df_sum.to_csv('compiled_gene_counts.csv', na_rep = 'NA' )
    print df_sum
get_data()
