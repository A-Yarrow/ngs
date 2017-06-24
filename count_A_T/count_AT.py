import sys
import pandas as pd
import matplotlib.pyplot as plt

def filter_fasta(file_in):
	
	filehandle = open(file_in, 'rb')
	fileout = open('non-polya-polyt.fasta', 'wb')
	gpA_90_pct = 0
	gpT_90_pct = 0
	nonT_nonA = 0
	A = [ ]; T = [ ]; C = [ ]; G = [ ]; N = [ ]
	#Make a dictionary of lists
	for line in filehandle:
		if line.startswith('>'):
			label = line
		elif not line.startswith('>'):
			A_bases = line.count('A') 
			T_bases = line.count('T') 
			G_bases = line.count('G') 
			C_bases = line.count('C') 
			N_bases = line.count('N') 
			A.append(A_bases), T.append(T_bases)
			G.append(G_bases), C.append(C_bases), N.append(N_bases) 
			bases = len(line)
			A_pct = [float(i) / bases for i in A]; T_pct = [float(i) / bases for i in T];
			C_pct = [float(i) / bases for i in C]; G_pct = [float(i) / bases for i in G];
			N_pct = [float(i) / bases for i in N]
			
			pct_a = float(A_bases) / float(bases)
			pct_t = float(T_bases) / float(bases)
			if pct_a >= 0.70:
				gpA_90_pct = gpA_90_pct + 1
			elif pct_t >= 0.70:
				gpT_90_pct = gpT_90_pct +1
			elif pct_a and pct_t <= 0.5:
				print line
				fileout.write(label)
				fileout.write(line)
				nonT_nonA = nonT_nonA + 1
			else:
	
				pass
	print 'number of reads with greater than 90% A:', gpA_90_pct
	print 'number of reads with greater than 90% T:', gpT_90_pct
	print 'number of reads with < 50% A or less than 50% T', nonT_nonA
	
	filehandle.close()
	fileout.close()
	return A_pct, T_pct, G_pct, C_pct, N_pct


def make_histogram():
	file_in = sys.argv[1]
	ylim = sys.argv[2]
	A_pct, T_pct, G_pct, C_pct, N_pct = filter_fasta(file_in)
	df = pd.DataFrame({'A':A_pct, 'T':T_pct, 'G':G_pct, 'C':C_pct, 'N':N_pct})
	df.plot(kind = 'hist', alpha = 0.4, bins = 20, ylim = [0, int(ylim)], xlim = \
	[0.05, 1]).legend(bbox_to_anchor=(0.3, 0.95))
	plt.show()
	plt.savefig(file_in[0:-5]+'.png')

make_histogram()