#!usr/bin/python

"""Author: Yarrow Madrona
   script to merge data tables on a common column label. Column labels should be in the first row of the file. Default is .txt tab delim
   Requires two inputs. csv or txt file that is your data set and a csv or txt file that the columns you want to add.
"""

import pandas as pd
import matplotlib.pyplot as plt
import argparse


#The function
def merge_data_tables_on(file1, file2, column_to_merge_on, column_label_list, sep1, sep2):
    print ('user supplied arguments are %r, %r, %r, %r:'%(file1, file2, column_to_merge_on, column_label_list))
    df_file1 = pd.read_csv(file1, sep=sep1)
    df_file2 = pd.read_csv(file2, sep=sep2, names=column_label_list.append(column_to_merge_on))
    new_df = df_file1.merge(df_file2, on=column_to_merge_on)
    new_df.to_csv(file1[0:-4]+'_merged.csv', index=False)
    

# --COMMAND LINE ARGUMENTS
parser = argparse.ArgumentParser(description='merge data tables')
parser.add_argument('--file1', '-f1', required=True, help='The file containing the data (.txt or .csv) you want to add suplimental data to')
parser.add_argument('--file2', '-f2', required=True, help='The file containing the data columns you will choose to merge to the first file')
parser.add_argument('--index', '-i', required=True, type=str, help='The column label that is common to data sets in file1 and file2. The data is merged on this label')
parser.add_argument('--labels', '-l', required=True, nargs='*', type=str, dest='label_list', help='The labels of columns from data in file2 that you would like to add to the data in file1 \
                    ex: --labels label1 label2 label3')
parser.add_argument('--sep_file1', '-s1', required=False, default=',', help='Delimiter to use for file1')
parser.add_argument('--sep_file2', '-s2', required=False, default='\t', help='Delimiter to use for file2')
args = parser.parse_args()
file1 = args.file1
file2 = args.file2
column_to_merge_on = args.index
sep1 = args.sep_file1
sep2 = args.sep_file2

if __name__ == "__main__":
    merge_data_tables_on(file1, file2, column_to_merge_on, args.label_list, sep1, sep2)
