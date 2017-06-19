#!/usr/bin/python
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn

df = pd.DataFrame()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
for (dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename.startswith('picard_rna_trimmed'):
            fhandle = open(filename, 'r')
            tmp_df_filename = pd.read_table(fhandle, header=8, sep="\t")
            ax.plot(tmp_df_filename['normalized_position'],\
            tmp_df_filename['All_Reads.normalized_coverage'], label=filename[25:30])
#plt.legend(loc = 'upper left')
plt.xlabel('Normalized position')
plt.ylabel('Normalized coverage')
plt.savefig('coverage_overlay.png')
plt.show()
