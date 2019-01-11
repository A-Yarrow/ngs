#usr/bin/python
"""Author: Yarrow Madrona
Take a multi-line aligned fasta and convert each entry into one long line
Assumes there is no header. If there is take it out.
"""
import sys
import collections
infile = sys.argv[1]

def conv_aln_single_line():
    file_out = open(infile[0:-4]+'_unstacked.txt', 'wb')
    d = collections.defaultdict(list)
    with open(infile, 'rb') as my_file:
        for line in my_file:
            line = line.strip().split()    
            if len(line) >= 2:
                d[line[0]].append(line[1])
    for record, sequence_list in d.iteritems():
        line = record+'\t'+("").join(sequence_list)
        print line+'\n'
        file_out.write(line+'\n')
    file_out.close()
   
conv_aln_single_line()