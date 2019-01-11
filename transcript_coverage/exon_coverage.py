#/usr/bin/python2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import numpy as np
import collections

#Make dictionary of base postions for each exon
def make_dict():
    parser = argparse.ArgumentParser(description='visualize exon coverage')
    parser.add_argument('-coverage_file', '-c', required=True, help='coverage calculated by bedtools coverage bed' )
    parser.add_argument('-bed', '-b', required=True, help='Bed file you want to plot coverage for')
    args = parser.parse_args()
    coverage_file = args.coverage_file
    bed_file = args.bed
    transcript_exon_list = []
    with open(bed_file, 'rb') as filehandle:
        for line in filehandle:
            line = line.rstrip().split('\t')
            chrom = line[0]
            start = int(line[1])
            end = int(line[2])
            number_exons = int(line[9])
            exon_sizes = line[10].rstrip(',').split(',')
            exon_sizes = np.array([int(i) for i in exon_sizes])
            exon_starts = line[11].rstrip(',').split(',')
            exon_starts = [int(i) for i in exon_starts]
            exons = range(1, number_exons+1)        
            exon_start_positions = np.array([i+start for i in exon_starts])
            exon_end_positions = np.add(exon_start_positions, exon_sizes)
            exon_start_end_dict = dict(zip(exons, zip(exon_start_positions, exon_end_positions)))
            transcript_exon_list.append(exon_start_end_dict)
    return transcript_exon_list, coverage_file, start, end #Should be the same for each transcript

def find_exons(base_position, transcript_exon_list):  
    for transcript_dict in transcript_exon_list:
        for key, value in transcript_dict.iteritems():
            exon = key
            start = value[0]
            end = value[1]
            if base_position < start or base_position > end:
                continue
            elif start <= base_position <= end:
                return exon
        
        
#Count the exon coverage from the coverage file produced by bed tools coverage
#Make a dataframe of each position and depth of coverage including a column for exons
def count_exon_coverage():        
    transcript_exon_list, coverage_file, start, end = make_dict()
    coverage_dict = collections.defaultdict(int)
    exon_coverage = []
    exon_all_transcripts_coverage = []
    with open(coverage_file, 'rb') as filehandle:
        for line in filehandle:
            line = line.rstrip().split('\t')
            position = int(line[6])+int(line[12])-1
            read_depth = int(line[13])
            coverage_dict[position] += read_depth
            
    #print (coverage_dict)
    df = pd.DataFrame.from_dict(coverage_dict, orient='index')
    df = df.sort_index().reset_index()
    df = df.rename(columns={'index': "Base position", 0: "No. reads"})
    #print(df.head())
    #return df
    df['Exon'] = df['Base position'].apply(find_exons, args=(transcript_exon_list,))
    df.to_csv(coverage_file[0:-4]+'_with_introns+exons.txt', index=False, sep='\t', na_rep='NaN')
    df_exons = df.dropna()
    df_exons.to_csv(coverage_file[0:-4]+'_exons_only.txt', index=False, sep='\t')
    
    g = sns.FacetGrid(df_exons, col="Exon", margin_titles=True)
    g.map(plt.scatter, "No. reads")
    g.add_legend()
    plt.show()
            
"""           
            for key, value in transcript_dict_cur.iteritems():
                key = exon
                value = st_stop
                print value, st_stop
        
            
            for exon_dict in transcript_exon_list:
                for key, value in exon_dict.iteritems():
                    exon_pos_list = range(value[0], value[1]+1)
                    exon_cov_dict = dict.fromkeys(exon_pos_list, 0)
                    if position in exon_cov_dict:  #if position is a key in the dictionary
                        exon_cov_dict[position] = read_depth
                    exon_coverage.append(exon_cov_dict)
                exon_all_transcripts_coverage.append(exon_coverage)
    print exon_coverage
    #print (exon_all_transcripts_coverage)
"""                
                         
count_exon_coverage()

        
        
    
    
        
        
    
