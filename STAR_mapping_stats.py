#!/usr/bin/python
import os
import numpy as np
import pandas as pd
#file_out = open('mapping_rna_stats.txt', 'w')

fields =['sample', 'AVG_READ_LGTH','UNQ_MAPPED_READS', 'Unique_mapped_%',\
'Mismatch rate per base', 'Deletion rate per base', 'Deletion average length',\
'Insertion rate per base', 'Insertion average length',  %
'Mult_loci','too_many', '%_too_many', '%unmapped-mism', '%unmapped-tooshort',\
        '%reads unmapped-other', 'chimeric_reads', '% chimeric_reads']

#for field in fields:
#    file_out.writelines(field+'\t')
#file_out.writelines('\n')

list1 = [fields]
s='Average input read length'
s2 = 'Uniquely mapped reads number'
s3='Uniquely mapped reads %'
s4='Number of reads mapped to multiple loci'
s5='Number of reads mapped to too many loci'
s6='% of reads mapped to too many loci'
s7='% of reads unmapped: too many mismatches'
s8='% of reads unmapped: too short'
s9='% of reads unmapped: other'
s10='Number of chimeric reads'
s11='% of chimeric reads'


for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        list_temp = []
        if filename.endswith('.final.out'):
            fhandle = open(filename, 'r')
            print filename
            list_temp.append(filename[13:18])
            for line in fhandle:
                if s in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                elif s2 in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                elif s3 in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                elif s4 in line:
                    line = line.strip().split()
                    print 'line:', line[8]
                    list_temp.append(line[8])
                elif s5 in line:
                    line = line.strip().split()
                    print 'line:', line[9]
                    list_temp.append(line[9])
                elif s6 in line:
                    line = line.strip().split()
                    print 'line:', line[9]
                    list_temp.append(line[9])
                elif s7 in line:
                    line = line.strip().split()
                    print 'line:', line[8]
                    list_temp.append(line[8])
                elif s7 in line:
                    line = line.strip().split()
                    print 'line:', line[6]
                    list_temp.append(line[6])
                elif s8 in line:
                    line = line.strip().split()
                    print 'line:', line[7]
                    list_temp.append(line[7])
                elif s9 in line:
                    line = line.strip().split()
                    print 'line:', line[6]
                    list_temp.append(line[6])
                elif s10 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
                elif s11 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
            fhandle.close()
            list1.append(list_temp)
            df = pd.DataFrame(list1)
df
df.to_csv('mapping_rna_stats.txt', sep='\t')
print open('mapping_rna_stats.txt', 'r').read()



