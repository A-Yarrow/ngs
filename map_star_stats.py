#!/usr/bin/python
import os
import numpy as np
import pandas as pd

fields =['sample', 'AVG_READ_LGTH','UNQ_MAPPED_READS', 'Unique_mapped read_%',\
        'Mismatch rate per base', 'Deletion rate per base', 'Deletion average length',\
        'Insertion rate per base', 'Insertion average length','Number of reads mapped to multiple loci',\
        'Reads mapped to too many loci','% reads mapped to too many loci','%unmapped-mism', '%unmapped-tooshort',\
        '%reads unmapped-other', 'chimeric_reads', '%_chimeric_reads']

list1 = []
s='Average input read length'
s2 ='Uniquely mapped reads number'
s3='Uniquely mapped reads %'
s4='Mismatch rate per base'
s5='Deletion rate per base'
s6='Deletion average length'
s7='Insertion rate per base'
s8='Insertion average length'
s9='Number of reads mapped to multiple loci'
s10='Number of reads mapped to too many loci'
s11='% of reads mapped to too many loci'
s12='% of reads unmapped: too many mismatches'
s13='% of reads unmapped: too short'
s14='% of reads unmapped: other'
s15='Number of chimeric reads'
s16='% of chimeric reads'

for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        list_temp = []
        if filename.endswith('.final.out'):
            fhandle = open(filename, 'r')
            print filename
            list_temp.append(str(filename[13:18]))
            for line in fhandle:
                if s in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                    print line, line[5]
                elif s2 in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                    print line, line[5]
                elif s3 in line:
                    line = line.strip().split()
                    list_temp.append(line[5])
                    print line, line[5]
                elif s4 in line:
                    line = line.strip().split()
                    print line, line[6]
                    list_temp.append(line[6])
                elif s5 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
                elif s6 in line:
                    line = line.strip().split()
                    print 'line:', line[4]
                    list_temp.append(line[4])
                elif s7 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
                elif s8 in line:
                    line = line.strip().split()
                    print 'line:', line[4]
                    list_temp.append(line[4])
                elif s9 in line:
                    line = line.strip().split()
                    print 'line:', line[8]
                    list_temp.append(line[8])
                elif s10 in line:
                    line = line.strip().split()
                    print 'line:', line[9]
                    list_temp.append(line[9])
                elif s11 in line:
                    line = line.strip().split()
                    print 'line:', line[9]
                    list_temp.append(line[9])
                elif s12 in line:
                    line = line.strip().split()
                    print 'line:', line[8]
                    list_temp.append(line[8])
                elif s13 in line:
                    line = line.strip().split()
                    print 'line:', line[7]
                    list_temp.append(line[7])
                elif s14 in line:
                    line = line.strip().split()
                    print 'line:', line[6]
                    list_temp.append(line[6])
                elif s15 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
                elif s16 in line:
                    line = line.strip().split()
                    print 'line:', line[5]
                    list_temp.append(line[5])
            fhandle.close()
            list1.append(list_temp)
            df = pd.DataFrame(list1, columns=fields)
df
df.to_csv('mapping_star_stats.txt', sep='\t', index=False)
print open('mapping_star_stats.txt', 'r').read()



