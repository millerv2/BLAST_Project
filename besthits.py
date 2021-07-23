from model import *
init()

proteins = Proteins.selectBy(species='Saccharomyces cerevisiae S288c')
accessions = []

#get all the accessions for the proteins from one proteome:
for p in proteins:
    accessions.append(p.accession)

#for each accession get the protein object associated with it.
for accession in accessions:
    prow = Proteins.byAccession(accession)
    
#iterate through the alignments involving the protein; take best alignment and check its best hit
    for a1 in prow.aligns_query:
        if a1.e_value<1e-10 and a1.query_align_length/a1.query.length>.75 and a1.ref_align_length/a1.reference.length>.75:
            besthit = a1.reference.accession
            query = a1.query
            refrow = Proteins.byAccession(besthit)
            for a2 in refrow.aligns_query:
                if a2.e_value<1e-10 and a2.query_align_length/a2.query.length>.75 and a2.ref_align_length/a2.reference.length>.75:
                    if a2.reference.accession == query.accession:
                        print(a2.query.name,'with accession',a2.query.accession,
                         'has best hit',a2.reference.name,'with accession',
                          a2.reference.accession,'having score',a2.score,
                          'and e_value',a2.e_value)
                        print(a1.query.name,'with accession',a1.query.accession,
                          'has best hit',a1.reference.name,'with accession',
                          a1.reference.accession,'having score',a1.score,
                          'and e_value',a1.e_value)
                        print(besthit,'and',a1.query.accession,'are mutual best hits.')
                        print("\n")
                break
        break
    



