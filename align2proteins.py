from model import *
import sys

init()

# check for proper inputs:
if len(sys.argv)<3:
    print("Please specify the accessions of two proteins to retreive their alignment!")
    sys.exit(1)

p1_accession = str(sys.argv[1])
p2_accession = str(sys.argv[2])

try:
    p1 = Proteins.byAccession(p1_accession)
    p2 = Proteins.byAccession(p2_accession)
except SQLObjectNotFound:
    print("At least one of specified proteins is not present in the database. Check your accessions.")
    sys.exit(1)

#tried with AAF45487.1 and NP_012367.1:
#fails with AAF45487.1 NP_012367. and AAF45487.1 NP_012363.1. Can demonstrate this.
#from the list of alignments with p1 as query protein, find alignment corresponding to p2:

Match = False
for a in p1.aligns_query:
    if a.reference == p2:
        print('The alignment of',a.query.name,'with accession',a.query.accession,'and',
              a.reference.name,'with accession',a.reference.accession,
              'has e-value',a.e_value,
              'and score',a.score)
        Match = True

if Match == False:
    print("No quality alignments for input proteins retrieved from database.")








