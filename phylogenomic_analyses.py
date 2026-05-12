#import needed modules
import os
import sys
import glob
import subprocess
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import Phylo

#folder: unaligned fasta files
indir = "unaligned_fastas"
#folder: aligned files
outdir = "aligned_fastas"
#folder: aligned files
if not os.path.exists(outdir):
    os.mkdir(outdir)
 
file_list = glob.glob(indir + "/*.fa")
print(file_list)

for i in file_list:
#new file path for each aligned file
    new_file_path = file.replace(indir, outdir)

#run mafft on each file
    aln_cmd = "mafft --auto --quiet " + file + " > " + new_file_path
    print(aln_cmd)
    # os.system(aln_cmd)
 
#loop through aligned files


#run iqtree on each alignment


#list: tree files


#loop through tree files


#read tree into python


#find outgroup tip


#root tree with outgroup


#find Bs Cr At tips


#test which pair is monophyletic


#store topology: each tree


#count: each topology


#figure for topology counts

