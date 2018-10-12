#!usr/bin/python
"""Author: Yarrow Madrona
    Takes two arguments
    benchmark csv gene list from CLC and a text file giving a list of csv's to compare benchmark to
    Outputs table giving filename and genes not identified in the benchmark.
    requires python 2.7 or 3 with matplotlib, pandas, and venn2 modules installed.
    If venn2 is not installed the script will still run but venn diagrams will not be produced.
"""

#--IMPORTS

import pandas as pd
import matplotlib.pyplot as plt
import argparse
import time
venn_bool = True
try:
    from matplotlib_venn import venn2
except ImportError:
    print ("You must install venn2 in order to view the venn diagrams. Try pip install matlotlib-venn or conda install -c conda-forge matplotlib-venn")
    time.sleep(3)
    venn_bool = False
    pass

#--Make the dataframes

def make_dataframes(benchmark, file_to_compare):
    df_benchmark = pd.read_csv(benchmark, header=0)
    df_benchmark[yaxis] = df_benchmark[yaxis].str.replace(',','').astype(float)
    benchmark_set = set(df_benchmark['Name'].tolist())
    df_compare = pd.read_csv(file_to_compare, header=0)
    df_compare[yaxis] = df_compare[yaxis].str.replace(',', '').astype(float)
    compare_set = set(df_compare['Name'].tolist())
    new_genes = compare_set - benchmark_set  #elements present in compare_set but not in bench mark set
    new_gene_list = list(new_genes)
    new_genes_data_frame = df_compare[df_compare['Name'].isin(new_gene_list)]
    benchmark_unique_genes = benchmark_set - compare_set #elements present in benchmark set but not name set
    benchmark_unique_genes_list = list(benchmark_unique_genes)
    benchmark_unique_genes_data_frame = df_benchmark[df_benchmark['Name'].isin(benchmark_unique_genes_list)]
    fileout = open(file_to_compare[0:-4]+'_unique_genes.txt', 'wb')
    for item in new_gene_list:
        fileout.write(item+'\n')
    fileout.close()
    new_genes_data_frame.to_csv(file_to_compare[0:-4]+'_unique_data.csv', index=False)
    print ("new transcripts/genes for %s: "%(file_to_compare), len(new_genes))
    print ("unique benchmark transcripts/genes for %s: "%(benchmark), len(benchmark_unique_genes))
    return df_benchmark, benchmark_unique_genes_data_frame, df_compare, new_genes_data_frame, xaxis, yaxis, ymax, benchmark_set, compare_set
    
#--Make the scatter plots

def make_plots(df_benchmark, df_benchmark_unique, df_compare, df_compare_unique, xaxis, yaxis, ymax):
    df_list = [df_benchmark, df_benchmark_unique, df_compare, df_compare_unique]
    df_benchmark.sort_values(by=[xaxis])
    df_benchmark.sort_values(by=[xaxis])
    df_compare.sort_values(by=[xaxis])
    df_compare_unique.sort_values(by=[xaxis])
    
    label_list = [benchmark[0:-4], benchmark[:-4]+'_unique', file_to_compare[:-4], file_to_compare[0:-4]+'_unique']
    label_tuple_bmark = zip(df_list[:2], label_list[:2])
    label_tuple_compare = zip(df_list[2:], label_list[2:])
    fig, ax = plt.subplots()
    fig2, ax2 = plt.subplots()
    fig3, ax3 = plt.subplots()
    fig4, ax4 = plt.subplots()
    fig5, ax5 = plt.subplots()
    
    for df, label in label_tuple_bmark:
        ax.scatter(df[xaxis].tolist(), df[yaxis].tolist(), alpha=0.25, label=label)
        ax.legend(loc='upper right', bbox_to_anchor = (0.75, 1), shadow=(True), ncol=1)
        ax.set_ylim(0, ymax)
        ax.set_xlabel(xaxis)
        ax.set_ylabel(yaxis)
    fig.savefig('_'.join(label_list[0:2]))
        
    for df, label in label_tuple_compare:
        ax2.scatter(df[xaxis].tolist(), df[yaxis].tolist(), alpha=0.25, label=label)
        ax2.legend(loc='upper right', bbox_to_anchor = (0.75, 1), shadow=(True), ncol=1)
        ax2.set_ylim(0, ymax)
        ax2.set_xlabel(xaxis)
        ax2.set_ylabel(yaxis)
    fig2.savefig('_'.join(label_list[2:]))  
    
    ax3.scatter(df_list[0][xaxis].tolist(), df_list[0][yaxis].tolist(), label=label_list[0], facecolors='none', edgecolor = 'blue')
    ax3.scatter(df_list[2][xaxis].tolist(), df_list[2][yaxis].tolist(), label=label_list[2], facecolors='none', edgecolor = 'orange')
    ax3.legend(loc='upper right', bbox_to_anchor = (0.75, 1), shadow=(True), ncol=1)
    ax3.set_ylim(0, ymax)
    ax3.set_xlabel(xaxis)
    ax3.set_ylabel(yaxis)
    fig3.savefig(label_list[0]+'_'+label_list[2])
    
    ax4.scatter(df_list[0][xaxis].tolist(), df_list[0][yaxis].tolist(), label=label_list[0], facecolors='none', edgecolor = 'blue')
    ax4.legend(loc='upper right', bbox_to_anchor = (0.75, 1), shadow=(True), ncol=1)
    ax4.set_ylim(0, ymax)
    ax4.set_xlabel(xaxis)
    ax4.set_ylabel(yaxis)
    fig4.savefig(label_list[0])
    
    ax5.scatter(df_list[2][xaxis].tolist(), df_list[2][yaxis].tolist(), label=label_list[2], facecolors='none', edgecolor = 'orange')
    ax5.legend(loc='upper right', bbox_to_anchor = (0.75, 1), shadow=(True), ncol=1)
    ax5.set_ylim(0, ymax)
    ax5.set_xlabel(xaxis)
    ax5.set_ylabel(yaxis)
    fig5.savefig(label_list[2])
    plt.close('all')
 
#--Make the venn diagram

def make_ven2_plot(benchmark_set, compare_set, benchmark, file_to_compare): 
    if venn_bool == True:
        plt.figure(figsize=(4,4))
        v = venn2([benchmark_set, compare_set], set_labels=(benchmark[0:-4], file_to_compare[0:-4]))
        plt.title(benchmark[0:-4]+' '+file_to_compare[0:-4]+' '+'venn diagram')
        plt.savefig(benchmark[0:-4]+'_'+file_to_compare[0:-4]+'_'+'venn_diagram')
        plt.show()
    elif venn_bool == False:
        plt.show()    
#--Call main

if __name__ == "__main__":
    
    # --COMMAND LINE ARGUMENTS
    parser = argparse.ArgumentParser(description='Find new transcripts')
    parser.add_argument('--benchmark_file', '-b', required=True, help='The file you want to compare all other files to')
    parser.add_argument('--file_to_compare', '-c', required=True, help='The file you want to compare with benchmark file')
    parser.add_argument('--xaxis', '-x', required=False, default='Transcript length', type=str, help='Enter the x-axis column name for data to plot. Use quotes if there is a \
                        quote or special character'+'\n'+'Default is Transcript length')
    parser.add_argument('--yaxis', '-y', required=False, default='RPKM', type=str, help='Enter the y-axis column name for data to plot. Use quotes if there is a \
                        quote or special character'+'\n'+'Default is RPKM')
    parser.add_argument('--ymax', '-ym', required=False, type=int, help='Sets a common y-max for all plots')
    args = parser.parse_args()
    benchmark = args.benchmark_file
    file_to_compare = args.file_to_compare
    xaxis = args.xaxis
    yaxis = args.yaxis
    ymax = args.ymax
    
    #--CALL FUNCTIONS
    df_benchmark, benchmark_unique_genes_data_frame, df_compare, new_genes_data_frame, xaxis, yaxis, ymax, benchmark_set, compare_set = make_dataframes(benchmark, file_to_compare)
    make_plots(df_benchmark, benchmark_unique_genes_data_frame, df_compare, new_genes_data_frame, xaxis, yaxis, ymax)
    make_ven2_plot(benchmark_set, compare_set, benchmark, file_to_compare)