mkdir trimmed;
for i in *_R1.fastq.gz
do
 SAMPLE=$(echo ${i} | sed "s/_R1\.fastq\.gz//")
 echo ${SAMPLE}_R1.fastq.gz ${SAMPLE}_R2.fastq.gz
cutadapt -a file:adapters.fasta -A file:adapters.fasta -m 15 --trim-n --max-n 0.7 -q20 -j 8 -u 12 -o trimmed/${SAMPLE}_R1_trimmed.fastq.gz -p trimmed/${SAMPLE}_R2_trimmed.fastq.gz ${SAMPLE}_R1.fastq.gz ${SAMPLE}_R2.fastq.gz
done
