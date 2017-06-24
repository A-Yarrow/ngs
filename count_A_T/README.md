This is a script to go through sequencing reads in fasta format and print out the number of reads with greater than 90% "A" bases, 
the number of reads with greater than 90% "T" bases, and the number of reads with less than 50% A or 50% T.
The script will also create a new multiple fasta containing all reads that have less than 50% A bases or less than 50% T bases.
A histogram is creating in png format that dipicts the number of reads (y-axis) that are a given percentage A, T, C, G or N (uncalled).

USAGE: python count_A_T arg1 arg2
arg1 is a fasta containing sequencing reads to be read
arg2 is the maximum y-limit of the histogram that will be created. Start with the number of reads in the input fasta
