#!/usr/bin/python
import os
import numpy as np
file_out = open('picard_gen_stats.txt', 'w')
names = []
ind2remove = [4,5,7,12,13,14,15,17,18,21,23,24,24,25]
fields =['SAMPLE', 'PAIR', 'TOTAL_READS','PF_READS','PF_READS_ALIGNED', 'PCT_PF_ALIGNED_READS',\
        'PF_HQ_ALIGNED_READS', 'PF_HQ_ALIGNED_BASES','PF_HQ_ALIGNED_Q20_BASES',\
        'MEAN_READ_LENGTH', 'BAD_CYCLES', 'STRAND_BALANCE',\
        'PCT_ADAPTER']
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            names.append(filename[15:29])

for field in fields:
    file_out.writelines(field+'\t')
file_out.writelines('\n')

for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            fhandle = open(filename, 'r')
            for line in fhandle:
                if line.startswith('PAIR'):
                    values = line.strip('\ ').strip('\n').split('\t')
                    values2 = [i.replace('\'', '') for i in values]
                    values2.insert(0, filename[15:27])
                    np.array(values2)
                    new_values = np.delete(values2, ind2remove)
                    #print new_values
                    #values4 = [float(i) for i in new_values]
                    s = ('\t').join(new_values)
                    file_out.writelines(s+'\n')
file_out.close()
#print open(file_out, 'r').readlines()
fhandle.close()



