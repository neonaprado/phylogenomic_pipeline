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
aln_list = glob.glob(outdir + "/*.fa")
print(aln_list)

for i in (aln_list)
    #run iqtree on each alignment
    tree_command = f"iqtree -s {aln} -m TEST -nt 2"
    print(tree_command)


#list: tree files
tree_list = glob.glob(outdir + "/*.treeFile")
print(tree_list)

topo_list = []

#loop through tree files
for i in tree_list:
    
    #read tree into python
    temp_tree = Phylo.read(tree, "newick")

    #find outgroup tip
    for i in temp_tree.get_terminals():
        if "Es_" in i.name:
            es_tip = i
            break

    #root tree with outgroup
    temp_tree.root_with_outgroup(es_tip)


      #find Bs Cr At tips
    all_terminal_branches = temp_tree.get_terminals()

    for t in all_terminal_branches:
        if "Bs_" in t.name:
            Bs_temp = t
        elif "Cr_" in t.name:
            Cr_temp = t
        elif "At_" in t.name:
            At_temp = t
        else:
            out_temp = t

    #test which pair is monophyletic
    P1_and_P2 = [Bs_temp, Cr_temp]
    P1_and_P3 = [Bs_temp, At_temp]
    P2_and_P3 = [Cr_temp, At_temp]

    #store topology: each tree
    if bool(temp_tree.is_monophyletic(P1_and_P2)):
        topo_str = "12top"
    elif bool(temp_tree.is_monophyletic(P1_and_P3)):
        topo_str = "13top"
    elif bool(temp_tree.is_monophyletic(P2_and_P3)):
        topo_str = "23top"
    else:
        topo_str = "Unknown"

    print(topo_str)
    topo_list.append(topo_str)


#count: each topology


#figure for topology counts

