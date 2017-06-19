#!/usr/bin/python
import os
import numpy as np
file_out = open('picard_rna_stats.txt', 'w')
names = []
ind2remove = [8,9,10,18,23,24,25,26]
fields =['SAMPLE','PF_BASES', 'PF_ALIGNED_BASES','RIBOSOMAL_BASES',\
        'CODING_BASES', 'UTR_BASES','INTRONIC_BASES','INTERGENIC_BASES', \
        'PCT_RIBOSOMAL_BASES', 'PCT_CODING_BASES', 'PCT_UTR_BASES', \
        'PCT_INTRONIC_BASES','PCT_INTERGENIC_BASES','PCT_MRNA_BASES', \
        'PCT_USABLE_BASES', 'MEDIAN_CV_COVERAGE','MEDIAN_5PRIME_BIAS', \
        'MEDIAN_3PRIME_BIAS', 'MEDIAN_5PRIME_TO_3PRIME_BIAS']
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            names.append(filename[15:27])

for field in fields:
    file_out.writelines(field+'\t')
file_out.writelines('\n')

for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.endswith('.txt'):
            fhandle = open(filename, 'r')
            for line in fhandle:
                if line.startswith('PF_BASES'):
                    line = fhandle.next()
                    values = line.strip(' ').strip('\n').split('\t')
                    values2 = [i.replace('\'', '') for i in values]
                    values2.insert(0, filename[15:27])
                    #print values2
                    np.array(values2)
                    new_values = np.delete(values2, ind2remove)
                    #print new_values
                    #values4 = [float(i) for i in new_values]
                    s = ('\t').join(new_values)
                    file_out.writelines(s+'\n')
file_out.close()
#print open(file_out, 'r').readlines()
fhandle.close()



