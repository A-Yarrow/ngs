#!/usr/bin/python2
import argparse
import os
import logging
import multiprocessing
from subprocess import call

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def find_file_pairs(directory_path):
    """
    Looks for read pairs, i.e. those file that contain R1 and R2. All files must have one of the following suffices:
    fastq, fq, fastq.gz, fq.gz
    :param directory_path: the directory where to look
    :return:two lists one for read 1 and one for read2
    """
    r1 = []
    r2 = []
    for f in os.listdir(directory_path):
        if f.endswith('fastq') or f.endswith('fq') or \
                f.endswith('fastq.gz') or f.endswith('fq.gz'):
            if "_R1_" in f or "_r1_" in f or "_R1" in f or "_r1" in f:
                r1.append(os.path.join(directory_path, f))
            elif "_R2_" in f or "_r2_" in f or "_R2" in f or "_r2" in f:
                r2.append(os.path.join(directory_path, f))
    r1.sort()
    r2.sort()
    print r1
    print r2
    return r1, r2


def main():
    parser = argparse.ArgumentParser(description="Execute the RNA-Seq pipeline using STAR")
    parser.add_argument("directory", help="to input directory containing read 1's and reads 2's")
    parser.add_argument("STAR_GENOME", help="where the STAR genome lives")

    args = parser.parse_args()

    cpu_count = multiprocessing.cpu_count() - 2
    command = ' '.join(['STAR --runMode alignReads '
                        '--outSAMtype BAM SortedByCoordinate '
                        '--twopassMode Basic '
                        '--quantMode GeneCounts '
                        '--chimOutType WithinBAM '
                        '--outReadsUnmapped Fastx',
                        '--chimSegmentMin 12 '
                        '--chimJunctionOverhangMin 12 '
                        '--alignSJDBoverhangMin 10 '
                        '--chimSegmentReadGapMax parameter 3 '
                        '--alignSJstitchMismatchNmax 5 -1 5 5 '
                        '--alignMatesGapMax 200000 '
                        '--alignIntronMax 200000 '
                        '--runThreadN', str(cpu_count),
                        '--genomeDir', args.STAR_GENOME])

    reads1, reads2 = find_file_pairs(args.directory)

    if reads1[0].endswith('gz') or reads1[0].endswith('zip'):
        command = ' '.join([command, '--readFilesCommand zcat'])

    for read_file_r1, read_file_r2 in zip(reads1, reads2):
        # call(' '.join(['fastqc', read_file_r1]), shell=True)
        # call(' '.join(['fastqc', read_file_r2]), shell=True)

        read_path, read_name = os.path.split(read_file_r1)
        read_name = read_name.replace('_L001_R1_001.fastq.gz', '')
        # # _L001_R1_001.fastq.gz
        out = os.path.join(read_path, read_name)

        STAR_command = ' '.join([command, '--readFilesIn', read_file_r1, read_file_r2, '--outFileNamePrefix', out])
        print STAR_command
        call(STAR_command, shell=True)

    logging.debug('Indexing files...')
    indexing_command = ''.join(['find ', args.directory, '/*.bam', "| parallel 'samtools index {}'"])
    logging.debug(indexing_command)
    call(indexing_command, shell=True)


if __name__ == "__main__":
    main()
