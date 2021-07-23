import sys
import Bio.SeqIO
from model import *

init(new=True)

# Read in the protein nodes, populate accession, description,and species
proteome_1 = open('yeast.aa')
proteome_2 = open('drosoph.aa')
for seq_record in Bio.SeqIO.parse(proteome_1, "fasta"):
    description = seq_record.description
    l = description.split('|')
    gi = l[1]
    accession = l[3]
    species = 'Saccharomyces cerevisiae S288c'
    name = l[4]
    length = len(seq_record.seq)
    p = Proteins(gi=gi,accession=accession,name=name,
                 length=length, species=species)
proteome_1.close()

for seq_record in Bio.SeqIO.parse(proteome_2, "fasta"):
    description = seq_record.description
    l = description.split('|')
    gi = l[1]
    accession = l[3]
    species = 'Drosophila melanogaster'
    des = l[4]
    des = des.split('[')
    name = des[0]
    name = name.split(')')
    name = name[1]
    length = len(seq_record.seq)
    p = Proteins(gi=gi,accession=accession,name=name,
               length=length,species=species)
proteome_2.close()




