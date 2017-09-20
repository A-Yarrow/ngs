#!/usr/bin/python
import pandas as pd
import os
import argparse
import matplotlib.pyplot as plt
import seaborn as sns


def get_data():
    parser = argparse.ArgumentParser(description='make plot of RPKM from many experiments. Inputs should be\
                                     CSV table with gene names in first column and RPKM in second column\
                                     This assumes that the first row is a header row and data starts on second row')
    parser.add_argument('-files', '-f', default = '.csv', required=False, help='text that is comon to all file names' )
    parser.add_argument('-skip_rows', '-sr', default = 0, required=False, help='rows to skip in the data relative to \
                        where the data starts. If the data starts immediately following the header, you should not skip any rows')
    args = parser.parse_args()
    common_name = args.files
    skip_rows = args.skip_rows
    df_sum = pd.DataFrame()
    for (dirname, dirs, files) in os.walk('.'):
        for filename in files:
            #filename = filename.lower()
            if common_name in filename:
                df = pd.read_csv(filename, skiprows=int(skip_rows), header=0, names = ['genes', filename+'_counts'])
                df_indexed = df.set_index(df['genes'])
                del df_indexed['genes']
                df_sum = pd.concat([df_sum, df_indexed], axis=1)
        df_sum.index.name = 'gene'
        df_sum.to_csv('compiled_gene_counts.txt', na_rep = 'NA' )
        print df_sum
get_data()